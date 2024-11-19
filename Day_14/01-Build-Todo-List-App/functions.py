import os

path = os.path.join(os.path.dirname(__file__), '../../files/todo_list/todos.txt')


def get_todos(filepath=path):
    """ Read a text file and return the list of to-do items """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=path):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


# La variable __name__ está definida internamente por Python. Su tipo es str.
# Si se ejecuta este fuente, su valor es "__main__" y el contenido del if se ejecuta
# Si se ejecuta otro fuente pepe.py, que importa este módulo con nombre
# functions.py, su valor es "functions" y el contenido del if no se ejecuta.
if __name__ == "__main__":
    print("Hello")
    print(get_todos())