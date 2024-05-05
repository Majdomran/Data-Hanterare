import PySimpleGUI as sg  # Importera PySimpleGUI för att skapa GUI
import subprocess  # Importera subprocess för att starta andra Python-skript
import os  # Importera os för att interagera med operativsystemet

def guide():
    # Funktion för att öppna guiden (guide.py) med subprocess
    subprocess.run([os.sys.executable, 'guide.py'])

def graph():
    # Funktion för att öppna grafikskriptet (graph.py) med subprocess
    subprocess.run([os.sys.executable, 'graph.py'])

def sort():
    # Funktion för att öppna sorteringskriptet (sort.py) med subprocess
    subprocess.run([os.sys.executable, 'sort.py'])

def data():
    # Funktion för att öppna importeringsskriptet (import_data.py) med subprocess
    subprocess.run([os.sys.executable, 'import_data.py'])

sg.theme('DarkRed')  # Välj temat för GUI-komponenter
sg.set_options(font='Franklin 14', button_element_size=(6, 3))  # Ställ in font och storlek för knappar

layout = [
    [sg.Text(
        '!! IMPORT DATA FIRST !!',  # Text som visas i GUI-fönstret
        font='Franklin 14',  # Font för texten
        justification='center',  # Justering av texten till mitten
        expand_x=True,  # Expandera textens bredd
        key='-TEXT-')],  # Unik nyckel för textkomponenten
    [sg.Button('GRAPH', expand_x=True), sg.Button('SORT', expand_x=True), sg.Button('GUIDE', expand_x=True), sg.Button('IMPORT DATA', expand_x=True)],
    # Knappar för olika åtgärder
]

window = sg.Window('Data Hanterare ~By Majd', layout)  # Skapa GUI-fönstret med definierat layout

while True:
    event, values = window.read()  # Lyssna på händelser och värden från GUI

    if event == sg.WIN_CLOSED:
        break  # Avsluta loopen om fönstret stängs

    # Öppna olika skript beroende på vilken knapp som tryckts
    if event == 'GRAPH':
        window.close()  # Stäng nuvarande GUI-fönster
        graph()  # Öppna grafikskriptet (graph.py)

    if event == 'SORT':
        window.close()  # Stäng nuvarande GUI-fönster
        sort()  # Öppna sorteringskriptet (sort.py)

    if event == 'GUIDE':
        window.close()  # Stäng nuvarande GUI-fönster
        guide()  # Öppna guiden (guide.py)

    if event == 'IMPORT DATA':
        window.close()  # Stäng nuvarande GUI-fönster
        data()  # Öppna importeringsskriptet (import_data.py)

window.close()  # Stäng GUI-fönstret när loopen avslutas
