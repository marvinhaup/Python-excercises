from tkinter import *

fenster = Tk()

class MyButton (Button):
    def aktion(self):
        print("Sie haben den Button gedrückt")

fenster.geometry("300x100")         # Größe des Tkinter-Fensters festlegen
fenster.title("Python-Kurs")        # Überschrift des Tkinter-Fensters festlegen
rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)  # Rahmen um das Tkinter-Fenster mit Hilfe der Frame() -Funktion erzeugen
rahmen.pack(fill = "both", expand = 1)  # Rahmen mit Hilfe der pack()-Funktion sichtbar machen, der das gesamte Fenster umfassen soll

label = Label(rahmen, text = "Wilkommen zum Python-Kurs!") # Label mit Hilfe der Label()-Funktion erzeugen
            # rahmen als übergeordnetes Objekt übergeben, damit er das Label auch ummfasst
label.grid(row = 1, column = 1, columnspan = 2, padx = 50, pady = 15) # Label wird in der Raster-darstellung in zeile 1 Spalte 1 dargestellt

button = Button(rahmen, text = "OK", command = fenster.destroy) # button-Objekt mithilfe der Button()-Funktion erstellen
            # rahmen als umschließendes Element angegeben, fenster.destroy als Aktion bei Betätigung des Knopfes
button.grid(row = 2, column = 1, pady = 10) # Knopf ird im Raster in Zeile 2 Spalte 1 dargestellt

button2 = MyButton(rahmen, text = "Action!") # rahmen als übergeordnetes Objekt, das den button umschließt
button2["command"] = button2.aktion # Bei Knopfdruck wird in der selbst definierten Klasse MyButton die Methode aktion() ausgeführt
button2.grid(row = 2, column = 2) # Knopf wird im Raster in Zeile 2 Spalte 2 dargestellt

fenster.mainloop()