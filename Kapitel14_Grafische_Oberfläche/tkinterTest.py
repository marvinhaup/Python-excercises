# Programm zum Testen der tkinter-Bibliothek

windowWidth = 300
windowHeight = 100

from tkinter import *

window = Tk()
window.title("Python-Kurs")
screenResolution = str(windowWidth) + 'x' + str(windowHeight)
window.geometry(screenResolution)
label = Label(text="Willkommen zum Python-Kurs!")
label.pack()

window.mainloop()