
# grade_configs.py

## Usage
The time consuming aspect of this grading process is opening each Packet Tracer
file and exporting the individual devices' configurations. This also requires naming
and storing each one of these files in a specified directory.

As far as I can tell - this is as quick as this process can be performed. (If you find
out otherwise, please share. I would lovvve to be wrong.)

So -- the process is -- open a Packet Tracer file and store the interested devices'
configs as studentFirstInitial_studentCompleteLastName_deviceName.txt in a specified
lab directory under 'grade_configs/configurations/'.

Then, execute grade_configs.py on that directory.
```python
grade_configs.py nat
```

The output is a _grades.txt file that contains the score of each student's
configuration based on the _required_statements.yml file.

### Create Lab directory.
```python
python grade_configs.py
```
Execute the script followed by the "./lab_directory". 

```python
config_grader.py lab_directory
```

### Required Folder Structure:
Create a directory under "configurations" and populate it with the required files.
Required Files:
+ _required_statements.yml
+ student_files.txt

Student Files:
+ Student files should be placed in the directory: ./configurations/lab_directory
```bash
.
├── README.md
├── configurations
│   └── example_lab_directory
│       ├── _required_statements.yml
│       ├── _test_complete.txt
│       ├── _test_missing.txt
│       └── a_student.txt
└── grade_configs.py
```