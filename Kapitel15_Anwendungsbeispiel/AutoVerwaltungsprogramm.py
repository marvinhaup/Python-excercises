from tkinter import * 
from anzeigen import * 
from hinzufügen import * 
from verkaufen import * 
from aendern import *

fenster = Tk()

fenster.geometry("700x350") 
fenster.title("Sortiment verwalten")
rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
rahmen.pack(fill="both", expand = 1)
button1 = Anzeigen(rahmen,text="Sortiment anzeigen", width = 20, height = 5) 
button1.config(font=("Arial", 12, "bold"))
button1["command"] = button1.anzeigen 
button1.place(x = 50, y = 50)
button2 = Hinzufuegen(rahmen,text="Fahrzeug hinzufügen", width = 20, height = 5) 
button2.config(font=("Arial", 12, "bold")) 
button2["command"] = button2.hinzufuegen 
button2.place(x = 430, y = 50)
button3 = Verkaufen(rahmen,text="Fahrzeug verkaufen", width = 20, height = 5) 
button3.config(font=("Arial", 12, "bold")) 
button3["command"] = button3.verkaufen 
button3.place(x = 50, y = 200)
button4 = Aendern(rahmen,text="Preis ändern", width = 20, height = 5) 
button4.config(font=("Arial", 12, "bold")) 
button4["command"] = button4.aendern 
button4.place(x = 430, y = 200)
fenster.mainloop()