import PySimpleGUI as sg


sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))



while True:
    layout = [
        [sg.Text(
            '!! IMPORT DATA FIRST !!',
            font='Franklin 26',
            justification='center',
            expand_x=True,
            key='-TEXT-')],
        [sg.Button('GRAPH', expand_x=True), sg.Button('SORT', expand_x=True), sg.Button('GUIDE', expand_x=True), sg.Button('IMPORT DATA', expand_x=True)],
    ]

    window = sg.Window('Data Hanterare ~By Majd', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'GRAPH':
            print('graph')
        
        if event == 'SORT':
            print('sort')
        
        if event == 'GUIDE':
            print('guide')
        
        if event == 'IMPORT DATA':
            print('import data')

    window.close() # MAJD