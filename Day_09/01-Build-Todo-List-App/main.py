import os

path = os.path.join(os.path.dirname(__file__), '../../files/todo_list/todos.txt')

while True:
    user_action = input("Type add, show (or sh), edit, complete or exit: ").lower().strip()
    
    if 'add' in user_action:
        todo = user_action[4:]
        
        with open(path, 'r') as file:
            todos = file.readlines()
        
        todos.append(todo + '\n')
        
        with open(path, 'w') as file:
            file.writelines(todos)
            
    elif 'show' in user_action or 'sh' in user_action:
        with open(path, 'r') as file:
            todos = file.readlines()
                    
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}- {item}"
            print(row)
            
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number -= 1
        
        with open(path, 'r') as file:
            todos = file.readlines()
        
        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'
        
        with open(path, 'w') as file:
            file.writelines(todos)
            
    elif 'complete' in user_action:
        number = int(user_action[9:])
        
        with open(path, 'r') as file:
            todos = file.readlines()
        
        index = number -1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        
        with open(path, 'w') as file:
            file.writelines(todos)
        
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
        
    elif 'exit' in user_action:
        break
    
    else:
        print("Command is not valid!")

        
print("Bye!")