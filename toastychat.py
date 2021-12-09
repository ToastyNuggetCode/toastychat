import PySimpleGUIQt as gui

gui.theme("Default1")

layout = [
    [gui.Text("ToastyChat")],
    [gui.Text("Enter A Username:")],
    [gui.Input(key = "_name_")],
    [gui.Button("Go!")],
    [gui.Input(key = "_input_")],
    [gui.Button("Send")],
    [gui.Text("",key = "_output_")],
]

window = gui.Window("ToastyChat", layout)
while True:
    event, values = window.read()

    name = values["_name_"]

    thing = values["_input_"]

    window["_output_"].update(thing)

    window["_input_"].update(name +":")
