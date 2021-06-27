from tkinter import *

class MyButton(Button):
    def aktion1(self):
        name = eingabe.get()        # speichern des im Entry()-Feld gespeicherten strings in der name-Variable
        print(name)                 # Ausgeben des durch den Nutzer eingegebenen Namens
        eingabe.delete(0,'end')     # Löschen des gesamten Inhalts im Entry()-Feldes
    def aktion2(self):  
        print(var.get())            # Ausgabe des checkbutton-Zustandes, unticked (0) oder ticked (1)

fenster = Tk()

fenster.geometry("300x300")         # Größe des Tkinter-Fensters festlegen
fenster.title("Python-Kurs")        # Überschrift des Tkinter-Fensters festlegen

rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)  # Rahmen um das Tkinter-Fenster mit Hilfe der Frame() -Funktion erzeugen
rahmen.pack(fill = "both", expand = 1)  # Rahmen mit Hilfe der pack()-Funktion sichtbar machen, der das gesamte Fenster umfassen soll

label = Label(rahmen, text=" Geben Sie ihren Namen ein: ") # Aufforderung seinen Namen einzugeben
label.pack()                        # anzeigen des Labes im Rahmen

eingabe = Entry(rahmen, bd = 2, width = 22) # Nutzerabfrage mit der Entry()-Funktion und abspeichern der Eingabe in der Variable Eingabe
eingabe.pack()                      # Anzeigen des Eingabefeldes, in diesem Fall unter der Eingabeaufforderung

button = MyButton(rahmen, text = "Eingabe") # Absenden des in das Eingabefeld eingegebenen Namens
button["command"] = button.aktion1  # Bei drücken des Knopfes wird aktion 1 der MyButton-Klasse ausgeführt
button.pack()                       # Anzeigen des Eingabe-Knopfes unter dem Eingabefeld

var = IntVar()                      # initiieren eines IntVar()-Objektes zum Abspeichern eines Wahrheitswertes
checkbutton = Checkbutton(rahmen, text = "Bestätigen", variable = var)  # initiieren eines checkbuttons mit der Checkbutton()-Methode
                                    # Abspeichern des chekbox-Zustandes in dem IntVar-Objekt "var", 0 oder 1
checkbutton.pack()                  # Anzeigen des Eingabe-Knopfes unter dem Eingabefeld

button2 = MyButton(rahmen, text = "Eingabe")    # Absenden des Checkbutton-Zustandes
button2["command"] = button.aktion2 # Ausführen der MyButton()-Methode aktion2(), welche den Zstand des Checkbuttons ausgibt
button2.pack()                      # anzeigen des zweiten Anzeige-Buttons

scrollbar = Scrollbar(rahmen)       # initiieren eines Scrollbar-Objektes, welches sich innerhalb des Rahmens befinden soll

liste = Listbox(rahmen, yscrollcommand = scrollbar.set) # initiieren eines Listbox-Elements, innerhalb des rahmens
                                    # Y-Achsen-scrollen bewirkt einen Aufruf der set-Methode innerhalb des Scrollbar-Objektes
for i in range(50):
    liste.insert(END, "Zeile " + str(i))    # Für jede Iteration wird eine neue Zeile mit Inhalt in das Listox-Element liste einefügt

scrollbar.config(command = liste.yview) # Beim nach unten Scrollen soll die Listbox nach unten gescrollt werden, zugriff per command
liste.pack(side="left")             # Die Listbox wird an der linken Seite angeheftet
scrollbar.pack(side = "left", fill = "y")   #Die Scrolbar wird ebenfalls links angeheftet und nach der y-Achse ausgerichtet

fenster.mainloop()