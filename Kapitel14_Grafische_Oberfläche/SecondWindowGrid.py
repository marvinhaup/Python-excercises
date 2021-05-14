# Programm zum Testen der tkinter-Bibliothek

from tkinter import *

# defining TK-window
window = Tk()

# Tkinter- window sizes
windowWidth = 300
windowHeight = 100


# creating an underclass, to define what to do on button-pressing
class MyButton(Button):
    def action(self):
        print("Sie haben den Knopf gedrückt!")

# setting up the window reaolution
screenResolution = (
    str(windowWidth) + "x" + str(windowHeight)
)  # workaround to avoid hard-coding tkinter windows
window.geometry(screenResolution)

# defining and adding a frame to the window
frame = Frame(window, relief="ridge", borderwidth=5)
frame.pack(fill="both", expand=1)

# adding strings into the tkinter output
window.title("Python-Kurs")
label = Label(frame, text="Willkommen zum Python-Kurs!")
label.grid(row = 1, column = 1, columnspan = 2, pady = 15, padx = 50)

# defining a tkinter-button
button2 = MyButton(frame, width = 10, text="Action!")
button2["command"] = button2.action
button2.grid(row = 2, column = 1, pady = 10)

button = Button(frame, text="OK", width = 10, command=window.destroy)
button.grid(row = 2, column = 2)

window.mainloop()