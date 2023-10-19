FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """
    Read the text files and return the
    list of to-do items.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):  # filepath,todos_args are parameters
    """
    Write to-do items in the text files.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


