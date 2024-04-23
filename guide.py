import PySimpleGUI as sg
import subprocess
import os

def main():
    subprocess.run([os.sys.executable, 'main.py'])

sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))



while True:
    layout = [
[sg.Text(
'''!! GUIDE !!
1. 
2.
3. 
4.
''',
            font='Franklin 14',
            justification='left',
            expand_x=True,
            key='-TEXT-')],
        [sg.Button('BACK TO MAIN', expand_x=True)],
    ]

    window = sg.Window('Data Hanterare ~By Majd', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        
        if event == 'BACK TO MAIN':
            main()
        

    window.close() # MAJD