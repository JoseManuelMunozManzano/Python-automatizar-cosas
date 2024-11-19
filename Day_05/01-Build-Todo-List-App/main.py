todos = []

while True:
    user_action = input("Type add, show (or sh), edit, complete or exit: ").lower().strip()
    
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show' | 'sh':
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