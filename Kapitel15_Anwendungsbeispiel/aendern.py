from tkinter import * 

class Aendern(Button):
  def aendern (self):
    class MyButton (Button):
      def aktion (self):
        artnr = eingabe1.get() 
        preisNeu = eingabe2.get() 
        f = open('dateien\sortiment.txt','r') 
        liste = f.readlines() 
        f.close() 
        geaendert = False 
        for i in range(len(liste)):
          if liste[i] == artnr+"\n":
            f = open('dateien\sortiment.txt','w') 
            liste[i+4] = preisNeu + "\n" 
            for linie in liste:
              f.write(linie)
            geaendert = True 
            break
        f.close() 
        fenster.destroy()
        
        if geaendert:
          fenster2 = Tk()
          fenster2.geometry("300x100") 
          fenster2.title("Preis geändert!")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5) 
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Preis wurde angepasst!") 
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy) 
          button2.pack(side = "bottom", pady = 5) 
          fenster2.mainloop()
        else:
          fenster2 = Tk()
          fenster2.geometry("300x100") 
          fenster2.title("Warnung!")
          rahmen2 = Frame(fenster2, relief="ridge", borderwidth=5) 
          rahmen2.pack(fill="both", expand = 1)
          label2 = Label(rahmen2, text="Artikelnummer nicht gefunden!") 
          label2.pack(expand = 1)
          button2 = Button(rahmen2,text="OK", command=fenster2.destroy) 
          button2.pack(side = "bottom", pady = 5) 
          fenster2.mainloop()
          
    fenster = Tk() fenster.geometry("500x400") 
    fenster.title("Preis ändern")
    rahmen = Frame(fenster, relief="ridge", borderwidth=5) 
    rahmen.pack(fill="both", expand = 1)
    label = Label(rahmen, text = "Neuen Preis festlegen:") 
    label.config(font=("Arial", 14, "bold")) 
    label.place(x = 80, y = 30)
    label1 = Label(rahmen, text = "Artikelnummer:") 
    label1.place(x = 100, y = 100) 
    eingabe1 = Entry(rahmen, bd = 2, width = 22) 
    eingabe1.place(x = 200, y = 100)
    label2 = Label(rahmen, text = "Neuer Preis:") 
    label2.place(x = 100, y = 140)
    eingabe2 = Entry(rahmen, bd = 2, width = 22) 
    eingabe2.place(x = 200, y = 140)
    button = MyButton(rahmen,text="Eingabe") 
    button["command"] = button.aktion 
    button.place(x = 180, y = 220) 
    fenster.mainloop()