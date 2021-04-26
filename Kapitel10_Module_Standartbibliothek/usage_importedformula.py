# Benutzen der miportierten Formel per  Ordneraufruf 

import modules.modul_bsp_formula

eingabe = eval(input("Geben Sie eine Zahl ein:"))
print(modules.modul_bsp_formula.formula(eingabe))

# Benutzen der Formel mit einmaligem Aufruf und abspeichern in neuer variable

import modules.modul_bsp_formula

importedformula = modules.modul_bsp_formula.formula
eingabe = eval(input("Geben Sie eine Zahl ein:"))
print(importedformula(eingabe))