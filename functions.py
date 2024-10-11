FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items
    """
    # filepath: parameter
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        print(todos_local)
    return todos_local


def write_todos(todos_arg, filepath = FILEPATH):
    print(todos_arg)
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


"""
print("I am outside")
print(__name__)
if __name__ == "__main__":
    print("hello from functions")
    print(get_todos())
"""
