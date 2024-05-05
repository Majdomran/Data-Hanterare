import PySimpleGUI as sg  # Importera PySimpleGUI för att skapa GUI
import subprocess  # Importera subprocess för att starta en annan Python-process
import os  # Importera os för att interagera med operativsystemet

selected_file_path = None  # Global variabel för att spara sökvägen till den valda filen

def main():
    # Funktion för att starta om huvudapplikationen (main.py) med Python
    subprocess.run([os.sys.executable, 'main.py'])

def import_data(values):
    # Funktion för att importera data från en fil baserat på värden från GUI
    global selected_file_path  # Använd global variabel för att spara filvägen
    file_path = values["file_path"]  # Hämta filvägen från GUI-input
    if file_path:
        selected_file_path = file_path  # Spara filvägen i global variabel
        # Visa popup-meddelande med bekräftelse på att data har importerats från filen
        sg.popup(f"Data imported from file:\n{selected_file_path}")

def read_data():
    # Funktion för att läsa data från den valda filen och visa innehållet i en scrollbar popup
    global selected_file_path  # Använd global variabel för att hämta filvägen
    if selected_file_path:  # Kontrollera om filvägen är vald
        try:
            with open(selected_file_path, 'r') as file:
                file_contents = file.read()  # Läs innehållet från filen
                # Visa innehållet i en scrollbar popup-ruta med titeln "File Contents"
                sg.popup_scrolled(file_contents, title='File Contents')
        except FileNotFoundError:
            # Visa felmeddelande om filen inte hittas
            sg.popup_error(f'Error: File "{selected_file_path}" not found.')

def create_gui():
    # Funktion för att skapa GUI-layouten för import av data
    sg.theme('DarkRed')  # Välj temat för GUI-komponenter
    sg.set_options(font='Franklin 14', button_element_size=(12, 2))  # Ställ in font och storlek för knappar

    # Definiera layouten för GUI-fönstret med text, knappar och filväljare
    layout = [
        [sg.Text('!! IMPORT DATA !!', font='Franklin 14', justification='center', expand_x=True, key='-TEXT-')],
        [sg.Button('IMPORT DATA'), sg.Button('READ DATA'), sg.Button('BACK TO MAIN')],
        [sg.InputText(key="file_path"), sg.FileBrowse()],  # Inputfält för filväg och filväljare
    ]

    return sg.Window('Data Hanterare ~By Majd', layout)  # Returnera GUI-fönstret med definierat layout

def main_gui():
    # Huvudfunktion för att köra GUI-interaktionen
    window = create_gui()  # Skapa GUI-fönstret med layouten

    while True:
        event, values = window.read()  # Lyssna på händelser och värden från GUI

        if event == sg.WIN_CLOSED:
            break  # Avsluta loopen om fönstret stängs

        if event == 'IMPORT DATA':
            import_data(values)  # Anropa funktion för att importera data när knappen 'IMPORT DATA' trycks

        if event == 'BACK TO MAIN':
            window.close()  # Stäng nuvarande GUI-fönster
            main()  # Starta om huvudapplikationen när knappen 'BACK TO MAIN' trycks

        if event == 'READ DATA':
            read_data()  # Anropa funktion för att läsa data när knappen 'READ DATA' trycks

    window.close()  # Stäng GUI-fönstret när loopen avslutas

# Kör main_gui direkt när filen importeras
main_gui()
