from tkinter import *

fenster = Tk()

fenster.geometry("300x100")         # Größe des Tkinter-Fensters festlegen
fenster.title("Python-Kurs")        # Überschrift des Tkinter-Fensters festlegen
rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)  # Rahmen um das Tkinter-Fenster mit Hilfe der Frame() -Funktion erzeugen
rahmen.pack(fill = "both", expand = 1)  # Rahmen mit Hilfe der pack()-Funktion sichtbar machen, der das gesamte Fenster umfassen soll

label = Label(rahmen, text = "Wilkommen zum Python-Kurs!") # Label mit Hilfe der Label()-Funktion erzeugen
            # rahmen als übergeordnetes Objekt übergeben, damit er das Label auch ummfasst
label.pack(expand = 1)              # label-Objek durch pack()-Methode im Fenster anzeigen lassen, mittig zentrieren mit expand=1

button = Button(rahmen, text = "OK", command = fenster.destroy) # button-Objekt mithilfe der Button()-Funktion erstellen
            # rahmen als umschließendes Element angegeben, fenster.destroy als Aktion bei Betätigung des Knopfes
button.pack(expand = 1)             # Zentrierung und Anzeigen des Buttons

fenster.mainloop()