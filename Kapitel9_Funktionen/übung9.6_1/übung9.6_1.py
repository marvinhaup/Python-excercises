# Programm zum vergleichen von zwei Zahlen und anschließendem Durchlauf in Zweierschritten

import Modules.modul_compare2numbers
myfunc = Modules.modul_compare2numbers.compformula

number1 = eval(input("Geben Sie ihre erste Zahl ein:"))
number2 = eval(input("Geben Sie ihre zweite Zahl ein:"))

myfunc(number1,number2)
