import functions
import FreeSimpleGUI as sg
import time
import os

sg.theme("DarkPurple4")

clock_label = sg.Text("", key="clock")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
# Añadimos una imagen como botón, con una tupla que indica su width y height 
# en px, y, para que el color del mouse no se confunda con el color de la
# imagen, indicamos el color del mouse.
add_button = sg.Button(image_source=f"{os.path.dirname(__file__)}/add.png",
                       image_size=(40, 40), mouseover_colors="LightBlue2",
                       tooltip="Add Todo", key="Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button(key="Complete",
                            image_source=f"{os.path.dirname(__file__)}/complete.png",
                            image_size=(70, 35), mouseover_colors="LightBlue2",
                            tooltip="Edit Todo")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                   layout=[[clock_label],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 20))
 
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'].lower() + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].lower() + "\n"
                
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select and item first", font=("Helvetica", 20))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select and item first", font=("Helvetica", 20))
        case 'todos':
            window['todo'].update(value=values['todos'][0]) 
        case "Exit" | sg.WIN_CLOSED:
            break

window.close()