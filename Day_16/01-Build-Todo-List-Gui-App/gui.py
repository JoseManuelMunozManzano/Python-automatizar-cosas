import functions
import FreeSimpleGUI as sg

# Creamos instancias de label, input box y botón
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

# Creamos una instancia de una ventana con su título y el layout con sus elementos (widgets).
# layout espera una lista de listas de instancias de objetos.
# Aquellos objetos que estén en la misma fila se deben incluir dentro de la misma lista.
window = sg.Window('My To-Do App', layout=[[label], [input_box, add_button]])
# read() es el método que muestra la ventana en pantalla.
# Se queda esperando a que interaccionemos con ella.
window.read()
# Cerrar la ventana
window.close()