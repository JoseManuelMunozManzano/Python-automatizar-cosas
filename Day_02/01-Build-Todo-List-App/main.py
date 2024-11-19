user_prompt = "Enter a todo: "

todos = []

while True:
    todo = input(user_prompt)
    # Probar con el texto: hola que tal, para ver las diferencias
    # entre capitalize() y title()
    print(todo.title())
    todo = todo.capitalize()
    todos.append(todo)
    print(todos)