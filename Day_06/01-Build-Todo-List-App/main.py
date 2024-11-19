import os

path = os.path.join(os.path.dirname(__file__), '../../files/todo_list/todos.txt')

while True:
    user_action = input("Type add, show (or sh), edit, complete or exit: ").lower().strip()
    
    match user_action:
        case 'add':
            # Indicamos el \n para que, al escribir en el fichero, cada tarea lo haga en
            # una línea diferente
            # Sería algo así: clean\n
            todo = input("Enter a todo: ") + "\n"
            
            file = open(path, 'r')
            todos = file.readlines()
            file.close()
            
            todos.append(todo)
            
            file = open(path, 'w')
            file.writelines(todos)
            file.close()
        case 'show' | 'sh':
            file = open(path, 'r')
            todos = file.readlines()
            file.close()
            
            for index, item in enumerate(todos):
                row = f"{index + 1}- {item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number -= 1
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of the todo to complete: "))
            todos.pop(number - 1)
        case 'exit':
            break
        case _:
            print("Hey, you entered an unknown command")
        
print("Bye!")