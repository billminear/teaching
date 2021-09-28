#!/usr/bin/env
"""
grade_configs.py
author: bill minear
purpose: iterates a directory of .txt files and lazily parses them for the cisco
         configuration statements found in _required_statements.yaml. for each file,
         an itemized score is generated. when all files are parsed, each generated
         scoring is written to ./_grades.txt.
         - .txt files are exported configurations from devices in assigned
           packet tracer labs.
usage:
- create _required_statements.yaml
- set CONFIGURATION_PATH to the location of the .txt files.
  - python grade_configs.py
- if CONFIGURATION_PATH not set, the directory can be passed in at the command line.
  - python grade_configs.py "directory_of_.txt_files"
"""
import os
import sys
import yaml
from pathlib import Path

### My Custom Configuration Path Variables
# LAB = "nat"
# STUDENT_CONFIG_ROOT = os.environ.get("STUDENT_CONFIG_PATH")
# COMPLETE_STUDENT_CONFIG_PATH = os.path.join(STUDENT_CONFIG_ROOT, LAB)
###

# ignore this until you have a suggested remedy.
NESTED_CONFIGURATION_DIRECTORY = "configurations"

try:
    lab_directory = sys.argv[1]

except IndexError:
    print("\nCreate new lab directory?")
    new = input("(y/n) ")

    if new.lower() != "y":
        print("\nExiting.\n")
        exit()

    lab_directory = input("\nLab directory name: ")
    lab_directory_path = os.path.join(
        ".",
        NESTED_CONFIGURATION_DIRECTORY,
        lab_directory,
    )

    if not os.path.isdir(lab_directory_path):
        os.mkdir(lab_directory_path)
        print(f"{lab_directory_path} created.")
        print("Modify files to your need.")
        print("Run script again with lab directory as the first argument.")
        print("Example: python grade_configs.py lab_directory\n")
        exit()

    else:
        print(f"\n{lab_directory_path} already exists.")
        print("Rerun the script with the directory as a the first argument.")
        print("Example: python grade_configs.py lab_directory\n")
        exit()

lab_directory_path = os.path.join(
    ".",
    NESTED_CONFIGURATION_DIRECTORY,
    lab_directory,
)

if not os.path.isdir(lab_directory_path):
    print(f"\n{lab_directory_path} not a directory.\n")
    exit()

output_lines = "-" * 14 + "\n"
output_lines += f"{lab_directory} grades\n"
output_lines += "-" * 14

files_to_skip = ["_required_statements.yml", "_grades.txt"]
files_to_read = [
    file.name for file in os.scandir(lab_directory_path) if file not in files_to_skip
]

for filename in files_to_read:
    student_file = os.path.join(lab_directory_path, filename)

    with open(student_file, "r") as student_config_file:
        student_config = student_config_file.readlines()

    lines_to_skip = ["!", ""]
    student_config = [
        line.strip() for line in student_config if line not in lines_to_skip
    ]
    student_config = set(student_config)

    required_statements_yaml = os.path.join(
        lab_directory_path, "_required_statements.yml"
    )
    with open(required_statements_yaml, "r") as required_statements_file:
        required_statements = yaml.safe_load(required_statements_file)

    statements = {
        required_statement["statement"] for required_statement in required_statements
    }
    missing_statements = statements.difference(student_config)

    # edge case for working around various delimeters in banner motds.
    # may be a more appropriate way to handle this. works for now.
    for line in student_config:
        if "banner" in line:
            missing_statements = [
                missing_statement
                for missing_statement in missing_statements
                if "banner" not in missing_statement
            ]

    score = 0
    for required_statement in required_statements:

        if required_statement["statement"] not in missing_statements:
            score += required_statement["score"]

    output_lines += "\n\n\n"
    output_lines += f"{filename}\n"
    output_lines += "-" * 14 + "\n"

    for required_statement in required_statements:
        statement = required_statement["statement"]

        if statement in missing_statements:
            value = "-----"
        else:
            value = required_statement["score"]
            value = f"{value:.2f}"

        output_lines += f" {value.zfill(5):^} | {statement}\n"

    output_lines += "-" * 14 + "\n"
    output_lines += f" {score:^.2f} | Total\n"

grade_file_path = os.path.join(lab_directory_path, "_grades.txt")
with open(grade_file_path, "w+") as grade_file:
    grade_file.write(output_lines)
