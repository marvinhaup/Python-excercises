a = eval(input("Bitte geben Sie den Warenbestand ein: "))
if a >= 100:
    print("Warenlager zu klein!")
elif a > 10:
    print("Es befinden sich ",a," Artikel im Warenlager")
elif a > 0:
    print("Warenbestand sehr niedrig, Ware nachbestellen!")
elif a == 0:
    print("Warenlager leer!!!")
else:
    print("ungültige Eingabe")