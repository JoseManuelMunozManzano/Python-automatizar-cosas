import FreeSimpleGUI as sg
from converters import convert

# Widgets
label1 = sg.Text("Enter feet")
input1 = sg.Input(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.Input(key="inches")

convert_button = sg.Button("Convert", key="convert")
result_label = sg.Text(key="result", text_color="red")

window = sg.Window("Convertor",
                   layout=[
                       [label1, input1],
                       [label2, input2],
                       [convert_button, result_label]
                   ])

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    
    print(event, values)
    feet = float(values["feet"])
    inches = float(values["inches"])
    meters = convert(feet, inches)
    
    window["result"].update(f"{meters} m")

window.close()