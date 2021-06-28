from tkinter import * 

class MyButton(Button):
    def aktion1(self):
         ergebnis = int(eingabe1.get()) + int(eingabe2.get()) 
         ergebnis = str(ergebnis)
         eingabe3.delete(0,'end')
         eingabe3.insert(0,ergebnis)
         eingabe1.delete(0,'end')
         eingabe2.delete(0,'end')

fenster = Tk()

fenster.geometry("300x300")
fenster.title("Addierer-Programm")

rahmen = Frame(fenster, relief = "ridge", borderwidth = 5)
rahmen.pack(fill="both", expand=1)

label1 = Label(rahmen, text="Summand 1")
label1.place(x = 50, y = 50 )

eingabe1 = Entry(rahmen, width = 15)
eingabe1.place(x = 150, y = 50)

label2 = Label(rahmen, text="Summand 2")
label2.place(x = 50, y = 100)

eingabe2 = Entry(rahmen, width = 15)
eingabe2.place(x = 150, y = 100)

label3 = Label(rahmen, text = "Summe:")
label3.place(x = 50, y = 200)

eingabe3 = Entry(rahmen, width = 15)
eingabe3.place(x = 150, y = 200)

button = MyButton(rahmen, text = "Addieren")
button["command"] = button.aktion1
button.place(x = 100, y = 150)

fenster.mainloop()