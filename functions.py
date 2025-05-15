def get_todos(filepath="remember.txt"):
    with open(filepath, "r") as f:
        todos = f.readlines()
    return todos
def write_todos(todos, filepath="remember.txt"):
    with open(filepath, "w") as f:
        f.writelines(todos)
