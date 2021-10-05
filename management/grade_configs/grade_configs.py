#!/usr/bin/env
import os
import sys
import yaml

from shutil import copytree
from pathlib import Path

try:
    lab_directory_name = sys.argv[1]

    if not os.path.isdir(lab_directory_name):
        print(f"\n{lab_directory_name} does not exist.")
        print("Rerun the script without an argument to create a new directory.\n")
        exit()

except IndexError:
    print("\nCreate new lab directory?")
    create_new_directory = input("(y/n) ")

    if create_new_directory.lower() != "y":
        print("\nExiting.\n")
        exit()

    lab_directory_name = input("\nLab directory name: ")
    lab_directory_path = os.path.join(".", lab_directory_name)

    if not os.path.isdir(lab_directory_path):
        new_path = copytree("example_lab_directory", lab_directory_path)
        configuration_file_path = os.path.join(new_path, "configuration_files")

        for file in os.scandir(configuration_file_path):
            os.remove(file.path)

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

        # # print(f"{lab_directory_path} created.")
        # print("Modify _required_statements to your need and add configurations to the configuration_files.")
        # print("Run script again with lab directory as the first argument.")
        # print("Example: python grade_configs.py lab_directory\n")
        # exit()

    else:
        print(f"\n{lab_directory_path} already exists.")
        print("Rerun the script with the directory as the first argument.")
        print("Example: python grade_configs.py lab_directory\n")
        exit()

# output_lines = "-" * 14 + "\n"
# output_lines += f"{lab_directory} grades\n"
# output_lines += "-" * 14

# files_to_skip = ["_required_statements.yml", "_grades.txt"]
# files_to_read = [
#     file.name for file in os.scandir(lab_directory_path) if file not in files_to_skip
# ]

configuration_file_path = os.path.join(lab_directory_name, "configuration_files")

for file in os.scandir(configuration_file_path):
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
