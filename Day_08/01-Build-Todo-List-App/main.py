import os

path = os.path.join(os.path.dirname(__file__), '../../files/todo_list/todos.txt')

while True:
    user_action = input("Type add, show (or sh), edit, complete or exit: ").lower().strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            
            with open(path, 'r') as file:
                todos = file.readlines()
            
            todos.append(todo)
            
            with open(path, 'w') as file:
                file.writelines(todos)
        case 'show' | 'sh':
            with open(path, 'r') as file:
                todos = file.readlines()
                        
            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}- {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            
            with open(path, 'r') as file:
                todos = file.readlines()
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            
            with open(path, 'w') as file:
                file.writelines(todos)
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            
            with open(path, 'r') as file:
                todos = file.readlines()
            
            index = number -1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            
            with open(path, 'w') as file:
                file.writelines(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
        
print("Bye!")