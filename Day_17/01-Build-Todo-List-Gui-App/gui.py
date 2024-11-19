import functions
import FreeSimpleGUI as sg

# Creamos instancias de distintos widgets.
# En la creación de input_box hemos indicado el nombre de la key que utilizaremos para gestionar
# qué hacemos durante un evento.
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# Creamos una instancia de una ventana con su título y el layout con sus elementos (widgets).
# Añadimos también la fuente, que es una tupla que contiene el nombre de la fuente y su tamaño.
# layout espera una lista de listas de instancias de objetos.
# Aquellos objetos que estén en la misma fila se deben incluir dentro de la misma lista.
# La lista del layout puede ser una (o varias) variable que se asigne a layout.
# De esta forma, podemos crear una lista dinámica de widgets.
window = sg.Window('My To-Do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 20))

while True:
    # read() es el método que muestra la ventana en pantalla.
    # Se queda esperando a que interaccionemos con ella.
    # Los eventos devuelven una tupla con el label de elemento y
    # un diccionario con el nombre de la key y el valor introducido.
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].lower() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            # Accedemos a la instancia de Listbox y actualizamos el contenido
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'].lower() + "\n"
            
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0]) 
        # Si pulsamos el icono de terminar el programa.           
        case sg.WIN_CLOSED:
            break

# Cerrar la ventana
window.close()