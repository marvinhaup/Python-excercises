from tkinter import * 

class MyButton(Button):
    def OeffneFenster(self):
        if checkVar.get() == 1:
            neuesFenster = Tk()
            neuesFenster.geometry("300x300")
            neuesFenster.title("neues Fenster")
            label1 = Label(neuesFenster, text="Ein neues Fenster wurde geöffnet!")
            label1.pack()

fenster = Tk()

fenster.geometry("350x300")
fenster.title("Conditional window opening")

rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)
rahmen.pack( fill = "both", expand = 1)

checkVar = IntVar()
checkbutton1 = Checkbutton(rahmen, text = "Bestätigen", variable = checkVar)
checkbutton1.pack()

button1 = MyButton(rahmen, text = "Fenster öffnen")
button1["command"] = button1.OeffneFenster
button1.pack()

fenster.mainloop()