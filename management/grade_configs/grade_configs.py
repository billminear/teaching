import os
import sys
import yaml

from shutil import copytree
from pathlib import Path

EXAMPLE_LAB_DIRECTORY_NAME = "example_lab"
CONFIGURATION_DIRECTORY_NAME = "configuration_files"

try:
    lab_directory_name = sys.argv[1]
    lab_directory_path = os.path.join(".", lab_directory_name)

    if not os.path.isdir(lab_directory_name):
        output_statement = f"\n{lab_directory_name} does not exist."
        output_statement += (
            "Rerun the script without an argument to create a new directory.\n"
        )
        print(output_statement)
        exit()

except IndexError:
    print("(example: py grade_config.py ospf")
    new_directory_response = input("\nCreate new lab directory? (y/n) ")

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
        # - create documentation on usage on the project's github.
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
        output_statement += "name as an argument to create the _grades.txt file containing grade output.\n"
        output_statement += "(example: py grade_configs.py ospf)\n"
        print(output_statement)
        exit()

    else:
        output_statement = f"\n{lab_directory_path} already exists."
        output_statement += "Rerun the script with the directory as the first argument."
        output_statement += "Example: python grade_configs.py lab_directory\n"
        print(output_statement)
        exit()

# output_lines = "-" * 14 + "\n"
# output_lines += f"{lab_directory} grades\n"
# output_lines += "-" * 14

configuration_directory = os.path.join(lab_directory_name, CONFIGURATION_DIRECTORY_NAME)

for file in os.scandir(configuration_directory):
    student_file = os.path.join(lab_directory_path, file.name)
    print(student_file)

#     with open(student_file, "r") as student_config_file:
#         student_config = student_config_file.readlines()

#     lines_to_skip = ["!", ""]
#     student_config = [
#         line.strip() for line in student_config if line not in lines_to_skip
#     ]
#     student_config = set(student_config)

#     required_statements_yaml = os.path.join(
#         lab_directory_path, "_required_statements.yml"
#     )
#     with open(required_statements_yaml, "r") as required_statements_file:
#         required_statements = yaml.safe_load(required_statements_file)

#     statements = {
#         required_statement["statement"] for required_statement in required_statements
#     }
#     missing_statements = statements.difference(student_config)

#     # edge case for working around various delimeters in banner motds.
#     # may be a more appropriate way to handle this. works for now.
#     for line in student_config:
#         if "banner" in line:
#             missing_statements = [
#                 if "banner" not in missing_statement
#             ]

#     score = 0
#     for required_statement in required_statements:

#         if required_statement["statement"] not in missing_statements:
#             score += required_statement["score"]

#     output_lines += "\n\n\n"
#     output_lines += f"{filename}\n"
#     output_lines += "-" * 14 + "\n"

#     for required_statement in required_statements:
#         statement = required_statement["statement"]

#         if statement in missing_statements:
#             value = "-----"
#         else:
#             value = required_statement["score"]
#             value = f"{value:.2f}"

#         output_lines += f" {value.zfill(5):^} | {statement}\n"

#     output_lines += "-" * 14 + "\n"
#     output_lines += f" {score:^.2f} | Total\n"

# grade_file_path = os.path.join(lab_directory_path, "_grades.txt")
# with open(grade_file_path, "w+") as grade_file:
#     grade_file.write(output_lines)
