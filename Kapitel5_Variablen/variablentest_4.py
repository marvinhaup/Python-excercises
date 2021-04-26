# Bespiel zur dynamischen Typisierung von Variablen

a = 5
print("Wert der Variablen a:",a)
print("Datentyp der Variablen a: ",type(a))
a = 5.5                             # Datentyp wird nachträglich angepasst
print("Wert der Variablen a:",a)
print("Datentyp der Variablen a: ",type(a))

b = 5
print("Wert der Variablen b:",b)
print("Datentyp der Variablen b: ",type(b))
b = b + 0.0                             # Datentyp wird nachträglich angepasst
print("Wert der Variablen b:",b)
print("Datentyp der Variablen b: ",type(b))

c = 5
print("Wert der Variablen c:",c)
print("Datentyp der Variablen c: ",type(c))
c = 'Hallo'                             # Datentyp wird nachträglich angepasst
print("Wert der Variablen c:",c)
print("Datentyp der Variablen c: ",type(c))
