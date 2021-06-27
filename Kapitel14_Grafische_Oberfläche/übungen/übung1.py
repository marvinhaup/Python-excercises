# Programm zur Eingabe von zwei werten und der anschließenden addition,
# als auch Ausgabe auf der Konsole

# Tkinter- window size Variables
windowWidth = 300
windowHeight = 100

# imported libraries
from tkinter import *

window = Tk()

# setting up the window reaolution
screenResolution = (str(windowWidth) + "x" + str(windowHeight))  # workaround to avoid hard-coding tkinter windows
window.geometry(screenResolution)



