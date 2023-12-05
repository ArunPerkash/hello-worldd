import os
import subprocess

def initialize_git_repository(project_name):
    # Step 2: Create a new Python project directory
    os.makedirs(project_name, exist_ok=True)
    os.chdir(project_name)

    # Step 3: Initialize Git repository
    subprocess.run(['git', 'init'], check=True)

    # Step 4: Create a .gitignore file
    with open('.gitignore', 'w') as gitignore_file:
        gitignore_file.write("""
# .gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
        """)

    # Step 5: Optional - Create a Python virtual environment
    subprocess.run(['python', '-m', 'venv', 'venv'], check=True)
    
    # Step 7: Add and commit files
    subprocess.run(['git', 'add', '.'], check=True)
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

    print(f"Git repository for {project_name} has been initialized successfully.")

if __name__ == "__main__":
    project_name = input("Enter the name of your Python project: ")
    initialize_git_repository(project_name)
