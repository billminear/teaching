import os
import sys
import yaml
from math import ceil
from shutil import copytree
from pathlib import Path

EXAMPLE_LAB_DIRECTORY_NAME = "example_lab"
CONFIGURATION_DIRECTORY_NAME = "configuration_files"
REQUIRED_STATEMENTS_FILE_NAME = "_required_statements.yml"
GRADE_FILE_NAME = "_grades.yml"

try:
    lab_directory_name = sys.argv[1]
    lab_directory_path = os.path.join(".", lab_directory_name)

    if not os.path.isdir(lab_directory_name):
        output_statement = f"\n{lab_directory_name} does not exist.\n"
        output_statement += (
            "Rerun the script without an argument to create it as a new directory.\n"
        )
        print(output_statement)
        exit()

except IndexError:
    new_directory_question = "\n"
    new_directory_question += "Create new lab directory? (y/n) "
    new_directory_response = input(new_directory_question)

    if new_directory_response.lower() != "y":
        print("\nExiting.\n")
        exit()

    lab_directory_name = input("\nLab directory name: ")
    lab_directory_path = os.path.join(".", lab_directory_name)

    if not os.path.isdir(lab_directory_path):
        # remember for later:
        # may be best to replace copying the entire directory, then deleting the
        # files within the configuration_files directory by filtering them out here
        # using the copytree "ignore" parameter.
        # - ignore requires a function and I don't have time for that right now.
        # - this works.
        new_path = copytree(EXAMPLE_LAB_DIRECTORY_NAME, lab_directory_path)

        configuration_directory = os.path.join(new_path, CONFIGURATION_DIRECTORY_NAME)

        for file in os.scandir(configuration_directory):
            os.remove(file.path)

        # important:
        # include link to documentation on usage located on the project's github.
        # - *create* documentation on usage on the project's github.
        output_statement = "\n"
        output_statement += "---" * 8 + "\n"
        output_statement += f"{lab_directory_path} created.\n"
        output_statement += "---" * 8 + "\n"
        output_statement += f"Modify {lab_directory_path}\\_required_statements.yml to meet your needs\n"
        output_statement += (
            "and add configuration files to the configuration_files directory.\n"
        )
        output_statement += "\n"
        output_statement += "Once you've completed the above, rerun the script with your lab directory\n"
        output_statement += (
            "as the argument to create the _grades.txt file containing grade output.\n"
        )
        output_statement += "\n"
        output_statement += "(example: py grade_configs.py ospf)\n"
        print(output_statement)
        exit()

    else:
        output_statement = f"\n{lab_directory_path} already exists."
        output_statement += "Rerun the script with the directory as the first argument."
        output_statement += "Example: python grade_configs.py lab_directory\n"
        print(output_statement)
        exit()

configuration_directory = os.path.join(lab_directory_path, CONFIGURATION_DIRECTORY_NAME)
required_statements_path = os.path.join(
    lab_directory_path, REQUIRED_STATEMENTS_FILE_NAME
)

student_dict = {}
for file in os.scandir(configuration_directory):

    student_name, device_name = file.name.split("_")
    device_name = device_name.strip(".txt")

    if student_name not in student_dict:
        student_dict[student_name] = {"total": 0}

    with open(file.path, "r") as student_file:
        student_configuration = student_file.readlines()

    lines_to_skip = ["!", ""]
    student_configuration_statements = [
        line.strip()
        for line in student_configuration
        if line.strip() not in lines_to_skip
    ]

    with open(required_statements_path, "r") as required_statements_file:
        required_statements = yaml.safe_load(required_statements_file)

    graded_statements = {}
    for statement in student_configuration_statements:

        # accepts *any* motd. lazy way of handling variance in delimiter selection.
        if statement.startswith("banner motd"):

            try:
                graded_statements.update(
                    {statement: required_statements[device_name].pop("banner motd")}
                )

            except KeyError:  # works. dunno if it's a great way to handle this though.
                pass

        elif statement in required_statements[device_name]:
            graded_statements.update(
                {statement: required_statements[device_name].pop(statement)}
            )

    graded_statements.update(
        {statement: 0 for statement in required_statements[device_name]}
    )

    for key, value in graded_statements.items():
        student_dict[student_name]["total"] += value
        student_dict[student_name]["total"] = max(
            0, student_dict[student_name]["total"]
        )
    student_dict[student_name]["total"] = ceil(student_dict[student_name]["total"])

    student_dict[student_name].update({device_name: graded_statements})

grade_file_path = os.path.join(lab_directory_path, GRADE_FILE_NAME)

with open(grade_file_path, "w") as grade_file:
    yaml.dump(student_dict, grade_file, sort_keys=False)
