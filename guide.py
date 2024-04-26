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
'''HOW TO RUN THE APP:
    1. OPEN THE FOLDER 
    2. OPEN TERMINAL
    3. TYPE "python main.py"
    4. DONE :)

HOW TO IMPORT DATA:
    1. PRESS THE BROWSE BUTTON
    2. SELLECT THE DATA FILE YOU WANT
    3. PRESS IMPORT DATA TO CHECK IF YOU CHOSE RIGHT FILE

HOW TO MAKE GRAPH:
    1.
    2.

HOW TO SORT:
    1.
    2.
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