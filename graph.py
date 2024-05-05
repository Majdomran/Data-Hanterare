import PySimpleGUI as sg  # Importera PySimpleGUI för att skapa GUI
import matplotlib.pyplot as plt  # Importera matplotlib för att skapa grafer
import tempfile  # Importera tempfile för att arbeta med temporära filer
import os  # Importera os för att interagera med operativsystemet
import subprocess

def mainsite():
    # Funktion för att starta om huvudapplikationen (main.py) med Python
    subprocess.run([os.sys.executable, 'main.py'])

def create_graph(data):
    # Extraherar namn och aktiviteter från data
    names = [entry[1] for entry in data]
    activities = [entry[2] for entry in data]

    # Räknar aktiviteter
    activity_counts = {}
    for activity in activities:
        if activity in activity_counts:
            activity_counts[activity] += 1
        else:
            activity_counts[activity] = 1

    # Skapar stapeldiagram
    plt.figure(figsize=(8, 5))
    plt.bar(activity_counts.keys(), activity_counts.values(), color='skyblue')
    plt.xlabel('Activity')
    plt.ylabel('Count')
    plt.title('Summer Activity Distribution')
    plt.tight_layout()

    # Sparar grafen till en temporär fil
    temp_file = os.path.join(tempfile.gettempdir(), 'summer_activity_plot.png')
    plt.savefig(temp_file)
    plt.close()

    return temp_file

def main():
    # Inställningar för GUI
    sg.theme('DarkRed')
    sg.set_options(font='Franklin 14', button_element_size=(12, 2))

    # GUI layout
    layout = [
        [sg.Text(
            '!! GRAPH MAKER !!',
            font='Franklin 14',
            justification='center',
            expand_x=True,
            key='-TEXT-')],
        [sg.Button('CREATE GRAPH', expand_x=True), sg.Button('BACK TO MAIN', expand_x=True)],
    ]

    # Skapar GUI-fönster
    window = sg.Window('Data Hanterare ~By Majd', layout)

    # Exempeldatapunkter
    data = [
        [1, 'Johanna', 'Plugga'],
        [2, 'Rickard', 'Springa'],
        [3, 'Michael', 'Programmera']
    ]

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break

        # Hanterar knapptryckningar
        if event == 'CREATE GRAPH':
            # Skapar grafen och visar en popup med filnamnet
            graph_file = create_graph(data)
            sg.popup('Graph Created!', 'Check the file: {}'.format(graph_file))

        if event == 'BACK TO MAIN':
            # Stänger nuvarande fönster och öppnar om main-fönstret
            window.close()
            mainsite()

    window.close()

# Kör main-funktionen
main()
