import PySimpleGUI as sg
import subprocess
import os
import pandas as pd


def main():
    subprocess.run([os.sys.executable, 'main.py'])

sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))



while True:
    layout = [
        [sg.Text(
            '!! IMPORT DATA !!',
            font='Franklin 14',
            justification='center',
            expand_x=True,
            key='-TEXT-')],
        [sg.Button('IMPORT DATA', expand_x=True),sg.Button('READ DATA', expand_x=True), sg.Button('BACK TO MAIN', expand_x=True)],
        [sg.InputText(key="file_path"), sg.FileBrowse()],
    ]

    window = sg.Window('Data Hanterare ~By Majd', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        if event == 'IMPORT DATA':
            file_path = values["file_path"]
            if file_path:
                sg.popup(f"Selected file: {file_path}")
        
        if event == 'BACK TO MAIN':
            main()

        if event == 'READ DATA':
            print('test')
    
        

    window.close() # MAJD