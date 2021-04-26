# Programm zur Veranschaulichung der Umwandlung von Datentypen

userinp = eval(input("Geben Sie bitte eine ganze Zahl ein: "))
userinp = float(userinp)
print("Die Zahl lautet: {} und ist vom datentyp: {}".format(userinp,type(userinp)))