import PySimpleGUI as sg  # Importera PySimpleGUI för att skapa GUI
import subprocess  # Importera subprocess för att starta andra Python-skript
import os  # Importera os för att interagera med operativsystemet

def main():
    # Funktion för att starta om huvudapplikationen (main.py) med Python
    subprocess.run([os.sys.executable, 'main.py'])

# Inställningar för GUI: Tema och fontstorlek för knappar
sg.theme('DarkRed')
sg.set_options(font='Franklin 14', button_element_size=(6, 3))

# GUI layout: Definiera layouten för GUI-fönstret
layout = [
    [sg.Text(
        '''HOW TO RUN THE APP:
        1. OPEN THE FOLDER 
        2. OPEN 'run.bat' FILE
        3. DONE :)

        HOW TO IMPORT DATA:
        1. PRESS THE BROWSE BUTTON
        2. SELECT THE DATA FILE YOU WANT
        3. PRESS IMPORT DATA TO CHECK IF YOU CHOSE THE RIGHT FILE
        4. PRESS READ DATA TO VIEW THE DATA
        5. DONE :)

        HOW TO MAKE GRAPH:
        1. PRESS ON GRAPH
        2. PRESS ON CREATE GRAPH
        3. DONE :)

        HOW TO SORT:
        1. PRESS ON SORT
        2. PRESS ON SORT
        3. DONE :)
        ''',
        font='Franklin 14',
        justification='left',
        expand_x=True,
        key='-TEXT-')],
    [sg.Button('BACK TO MAIN', expand_x=True)],  # Knapp för att gå tillbaka till huvudmenyn
]

# Skapa GUI-fönster med titeln 'Data Hanterare ~By Majd' och definierad layout
window = sg.Window('Data Hanterare ~By Majd', layout)

while True:
    event, values = window.read()  # Lyssna på händelser och värden från GUI

    if event == sg.WIN_CLOSED:
        break  # Avsluta loopen om fönstret stängs

    # Hantera knapptryckningar
    if event == 'BACK TO MAIN':
        window.close()  # Stäng nuvarande GUI-fönster
        main()  # Starta om huvudapplikationen när knappen 'BACK TO MAIN' trycks

window.close()  # Stäng GUI-fönstret när loopen avslutas
