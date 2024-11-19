import os

path = os.path.join(os.path.dirname(__file__), '../../files/todo_list/todos.txt')

def get_todos(filepath):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show (or sh), edit, complete or exit: ").lower().strip()
    
    if user_action.startswith('add'):
        todo = user_action[4:]
        
        todos = get_todos(filepath=path)
        
        todos.append(todo + '\n')
        
        write_todos(filepath=path, todos_arg=todos)
            
    elif user_action.startswith('show') or user_action.startswith('sh'):
        todos = get_todos(path)
                    
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            print(row)
            
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1
            
            todos = get_todos(path)
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            write_todos(path, todos)
            
        except ValueError:
            print("Your commmand is not valid.")
            continue
            
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            todos = get_todos(path)
            
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            write_todos(path, todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        
    elif user_action.startswith('exit'):
        break
    
    else:
        print("Command is not valid!")

        
print("Bye!")