import PySimpleGUI as sg

"""
    Dashboard using blocks of information.
    Copyright 2020 PySimpleGUI.org
"""

BLACK_COLOR = '#000000'
DARK_COLOR = '#1B2838'
BPAD_TOP = ((20,20), (20, 10))
BPAD_LEFT = ((20,10), (0, 10))
BPAD_LEFT_INSIDE = (0, 10)
BPAD_RIGHT = ((10,20), (10, 20))

top_banner = [[sg.Text('Dashboard'+ ' '*100, font='Any 20', background_color=DARK_COLOR),
               sg.Text('Tuesday 9 June 2020', font='Any 20', background_color=DARK_COLOR),
               sg.Button('X')]]

top  = [[sg.Text('The Weather Will Go Here', justification='c', pad=BPAD_TOP, font='Any 20')],
            [sg.T(f'{i*25}-{i*34}') for i in range(7)],]

block_3 = [[sg.Text('Block 3', font='Any 20')],
            [sg.Input(), sg.Text('Some Text')],
            [sg.Button('Go')]  ]


block_2 = [[sg.Text('Block 2', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.Image(data=sg.DEFAULT_BASE64_ICON)]  ]

block_4 = [[sg.Text('Block 4', font='Any 20')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')],
            [sg.T('This is some random text')]]


layout = [[sg.Column(top_banner, pad=(0,0), background_color=DARK_COLOR)],
          [sg.Column(top, size=(920, 90), pad=BPAD_TOP, background_color=DARK_COLOR)],
          [sg.Column([[sg.Column(block_2, size=(450,150), pad=BPAD_LEFT_INSIDE)],
                      [sg.Column(block_3, size=(450,150),  pad=BPAD_LEFT_INSIDE)]], pad=BPAD_LEFT, 
background_color=BLACK_COLOR),
           sg.Column(block_4, size=(450, 320), pad=BPAD_RIGHT)]]

window = sg.Window('Dashboard PySimpleGUI-Style', layout, background_color=BLACK_COLOR, 
element_justification='center', resizable=True, finalize = True)
window.Maximize()

while True:             # Event Loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'X':
        break

window.close()
