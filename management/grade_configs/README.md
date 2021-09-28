
# grade_configs.py

## Usage
1. Create new lab directory: python grade_configs.py 
2. Add student configs to "./lab_directory"
   a. filename should follow "studentFirstInitial_studentCompleteLastName.txt" scheme.
2. 

Execute the script followed by the "./lab_directory". 

```python
config_grader.py lab_directory
```

### Required Folder Structure:
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