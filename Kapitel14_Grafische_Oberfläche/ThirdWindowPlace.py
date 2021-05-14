# Programm zum Testen der tkinter-Bibliothek

from tkinter import *

# defining TK-window
window = Tk()

# Tkinter- window sizes
windowWidth = 500
windowHeight = 300


# creating an underclass, to define what to do on button-pressing
class MyButton(Button):
    def action(self):
        print("Sie haben den Knopf gedrückt!")

class MyInputButton(Button):

    def action0(self):
        name = userInput.get()
        print(name)
        userInput.delete(0,'end')

    def action1(self):
        print(var.get())
    

# setting up the window reaolution
screenResolution = (str(windowWidth) + "x" + str(windowHeight))  # workaround to avoid hard-coding tkinter windows
window.geometry(screenResolution)

# defining and adding a frame to the window
frame = Frame(window, relief="ridge", borderwidth=5)
frame.pack(fill="both", expand=1)

# adding strings into the tkinter output
window.title("Python-Kurs")
"""
label0 = Label(frame, text="Willkommen zum Python-Kurs!")
label0.place(x = 60, y = 20)
"""
label1 = Label(frame, text = "Geben Sie ihren Namen ein:")
label1.pack()

# creating an input field
userInput = Entry(frame, bd = 2, width = 22)
userInput.pack()

# defining a tkinter-button
"""
button0 = Button(frame, text="OK", width = 10, command=window.destroy)
button0.place(x = 170, y = 60)

button1 = MyButton(frame, width = 10, text="Action!")
button1["command"] = button1.action
button1.place(x = 40, y = 60)
"""
var = IntVar()
checkbutton = Checkbutton(frame, text = "Bestätigen", variable = var)
checkbutton.pack()
button2 = MyInputButton(frame, text = "Eingabe")
button2["command"] = button2.action1
button2.pack()

# adding elements dor navigation
scrollbar = Scrollbar(frame)
myList = Listbox(frame, yscrollcommand = scrollbar.set)
for i in range(50):
    myList.insert(END, "Zeile " + str(i))
myList.pack(side = "left")
scrollbar.pack(side = "left", fill = "y")


window.mainloop()