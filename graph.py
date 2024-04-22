import PySimpleGUI as sg


sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))



while True:
    layout = [
        [sg.Text(
            '!! GRAPH MAKER !!',
            font='Franklin 14',
            justification='center',
            expand_x=True,
            key='-TEXT-')],
        [sg.Button('CREATE GRAPH', expand_x=True), sg.Button('BACK TO MAIN', expand_x=True)],
    ]

    window = sg.Window('Data Hanterare ~By Majd', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'GRAPH':
            print('graph')
        
        if event == 'BACK':
            print('BACK')
        

    window.close() # MAJD