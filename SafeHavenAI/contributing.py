```python
# SafeHavenAI/contributing.py

def fork_repository():
    print("Fork the repository from https://github.com/safehavenai.git")

def create_new_branch(branch_name):
    print(f"Create a new branch named {branch_name} for your feature or bug fix.")

def make_changes():
    print("Make your changes to the code.")

def ensure_tests_pass():
    print("Ensure all tests pass before committing your changes.")

def commit_push_changes():
    print("Commit and push your changes to your forked repository.")

def submit_pull_request():
    print("Submit a pull request detailing your changes.")

def adhere_code_of_conduct():
    print("Please ensure that your contributions adhere to the code of conduct.")

def contribute():
    branch_name = input("Enter the name of your new branch: ")
    fork_repository()
    create_new_branch(branch_name)
    make_changes()
    ensure_tests_pass()
    commit_push_changes()
    submit_pull_request()
    adhere_code_of_conduct()

if __name__ == "__main__":
    contribute()
```