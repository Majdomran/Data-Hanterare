import PySimpleGUI as sg  # Importera PySimpleGUI för att skapa GUI
import subprocess  # Importera subprocess för att starta andra Python-skript
import os  # Importera os för att interagera med operativsystemet
import csv  # Importera csv för att läsa och skriva CSV-filer

def sort_data():
    try:
        data = []
        with open('Matteprov.csv', 'r') as file:
            reader = csv.reader(file)
            header = next(reader)  # Läs den första raden (rubrikerna) i CSV-filen
            for row in reader:
                data.append(row)  # Lägg till varje rad i en lista

        # Sortera data baserat på första kolumnen (antagligen ID)
        sorted_data = sorted(data, key=lambda x: x[0])

        # Skriv det sorterade datat till en ny CSV-fil
        with open('sorted_data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)  # Skriv rubrikerna till den nya filen
            writer.writerows(sorted_data)  # Skriv det sorterade datat till den nya filen

        sg.popup('Data sorted successfully!', title='Sort Data')  # Visa popup-meddelande vid lyckad sortering
    except Exception as e:
        sg.popup_error(f'Error occurred: {e}', title='Sort Data Error')  # Visa felmeddelande vid fel under sortering

def main():
    subprocess.run([os.sys.executable, 'main.py'])  # Starta huvudapplikationen (main.py) med subprocess

sg.theme('DarkRed')  # Välj temat för GUI-komponenter
sg.set_options(font='Franklin 14', button_element_size=(6, 3))  # Ställ in font och storlek för knappar

layout = [
    [sg.Text(
        '!! SORT !!',  # Rubrik för GUI-fönstret
        font='Franklin 14',  # Font för texten
        justification='center',  # Justering av texten till mitten
        expand_x=True,  # Expandera textens bredd
        key='-TEXT-')],  # Unik nyckel för textkomponenten
    [sg.Button('SORT DATA', expand_x=True), sg.Button('BACK TO MAIN', expand_x=True)],  # Knappar för att sortera data eller gå tillbaka till huvudmenyn
]

window = sg.Window('Data Hanterare ~By Majd', layout)  # Skapa GUI-fönstret med definierat layout

while True:
    event, values = window.read()  # Lyssna på händelser och värden från GUI

    if event == sg.WIN_CLOSED:
        break  # Avsluta loopen om fönstret stängs

    if event == 'SORT DATA':
        sort_data()  # Anropa funktionen för att sortera data när knappen 'SORT DATA' trycks
        
    if event == 'BACK TO MAIN':
        window.close()  # Stäng nuvarande GUI-fönster
        main()  # Starta huvudapplikationen när knappen 'BACK TO MAIN' trycks

window.close()  # Stäng GUI-fönstret när loopen avslutas
