import PySimpleGUI as sg
import subprocess
import os

def guide():
    subprocess.run([os.sys.executable, 'guide.py'])

def graph():
    subprocess.run([os.sys.executable, 'graph.py'])

def sort():
    subprocess.run([os.sys.executable, 'sort.py'])

def data():
    subprocess.run([os.sys.executable, 'import_data.py'])

sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))



while True:
    layout = [
        [sg.Text(
            '!! IMPORT DATA FIRST !!',
            font='Franklin 14',
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
            window.close()
            graph()
        
        if event == 'SORT':
            window.close()
            sort()
        
        if event == 'GUIDE':
            window.close()
            guide()
        
        if event == 'IMPORT DATA':
            window.close()
            data()