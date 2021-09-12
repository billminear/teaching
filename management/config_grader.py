'''
config_grader.py
author: bill minear

'''
import os
import sys
import yaml
from pathlib import Path

try:
    lab_directory = sys.argv[1]

except:
    print('Provide an argument at the command line.')

configuration_directory = 'configurations'
config_path = os.path.join(Path.home(), 'Desktop', configuration_directory, lab_directory)
required_statements_yaml = os.path.join(config_path, '_required_statements.yml')
grade_file_path = os.path.join(config_path, 'grades.txt')

ignore_files = ['_required_statements.yml', 'grades.txt']
output_lines = '-'*14 + '\n'
output_lines += f'{lab_directory} grades\n'
output_lines += '-'*14
for file in os.scandir(config_path):
    
    if file.name not in ignore_files:
        student_file = os.path.join(config_path, file.name)

        with open(student_file, 'r') as student_config_file:
            student_config = student_config_file.readlines()

        lines_to_skip = ['!', '']
        student_config = [line.strip() for line in student_config if line not in lines_to_skip]
        student_config = set(student_config)

        with open(required_statements_yaml, 'r') as required_statements_file:
            required_statements = yaml.safe_load(required_statements_file)

        statements = {required_statement['statement'] for required_statement in required_statements}
        missing_statements = statements.difference(student_config)

        for line in student_config:
            if 'banner' in line:
                missing_statements = [missing_statement for missing_statement in missing_statements if 'banner' not in missing_statement]

        score = 0
        for required_statement in required_statements:

            if required_statement['statement'] not in missing_statements:
                score += required_statement['score']

        output_lines += '\n\n\n'
        output_lines += f'{file.name}\n'
        output_lines += '-'*14 + '\n'
        for required_statement in required_statements:
            statement = required_statement['statement']

            if statement in missing_statements:
                value = '-----'

            else:
                value = required_statement['score']
                value = f'{value:.2f}'

            output_lines += f' {value.zfill(5):^} | {statement}\n'

        output_lines += '-'*14 + '\n'
        output_lines += f' {score:^.2f} | Total\n'

with open(grade_file_path, 'w+') as grade_file:
    grade_file.write(output_lines)
