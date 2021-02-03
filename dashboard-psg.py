import PySimpleGUI as sg

"""
    Dashboard using blocks of information.
    Copyright 2020 PySimpleGUI.org
"""

BLACK = '#000000'
DARK_HEADER_COLOR = '#1B2838'

layout = [[sg.Text('Block 3', font='Any 20')], [sg.Button('Go'), sg.Button('Exit')]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, background_color=BLACK, resizable=True, finalize = True)
window.Maximize()

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
