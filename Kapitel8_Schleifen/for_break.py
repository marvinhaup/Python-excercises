mylist = [3,4,5,6,7,8,9,1]

geswert = eval(input("Welcher Wert soll gesucht werden?: "))
for n in mylist:
    if n == geswert:
        print("Wert wurde gefunden.")
        break
    print(n)
else:
    print("Der eingegebene Wert ist nicht in der Liste enthalten!")