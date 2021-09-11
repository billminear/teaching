'''
config_grader.py
author: bill minear

'''
import os
import yaml
from math import ceil
from pathlib import Path

lab_directory = 'acl'
configuration_directory = 'configurations'
config_path = os.path.join(Path.home(), 'Desktop', configuration_directory, lab_directory)
required_statements = os.path.join(config_path, '_required_statements.yml')

ignore_files = ['_required_statements.yml']
for file in os.scandir(config_path):
    
    if file.name not in ignore_files:
        student_file = os.path.join(config_path, file.name)

        with open(student_file, 'r') as student_config_file:
            student_config = student_config_file.readlines()

lines_to_remove = ['!', '']
student_config = [line.strip() for line in student_config if line not in lines_to_remove]
student_config = set(student_config)

with open(required_statements, 'r') as required_statements_file:
    statement_objects = yaml.safe_load(required_statements_file)

statements = {statement_object['statement'] for statement_object in statement_objects}
missing_statements = statements.difference(student_config)

score = 0
for statement_object in statement_objects:
    if statement_object['statement'] not in missing_statements:
        score += statement_object['value']

total_score = ceil(score)

print(total_score)