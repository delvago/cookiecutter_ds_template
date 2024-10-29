import sys 
project_name = '{{ cookiecutter.project_name }}'
if not project_name:
    print(f"ERROR: '{project_name}' is not a valid Python project name!")
    sys.exit(1)