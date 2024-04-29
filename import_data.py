import PySimpleGUI as sg
import subprocess
import os


def main():
    subprocess.run([os.sys.executable, 'main.py'])

def import_data(file_path):
    if file_path:
        with open(file_path, 'r') as file:
            data = file.read()
        return data
    else:
        return None

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
                global selected_file_path
                selected_file_path = file_path
                sg.popup(f"Data imported from file:\n{selected_file_path}")

        if event == 'BACK TO MAIN':
            window.close()
            main()

        if event == 'READ DATA':
            if selected_file_path:
                try:
                    with open(selected_file_path, 'r') as file:
                        file_contents = file.read()
                        sg.popup_scrolled(file_contents)
                except FileNotFoundError:
                    sg.popup_error(f'Error: File "{selected_file_path}" not found.')