eingabe = eval(input("Geben Sie eine zu verdoppelnde Zahl ein: "))
while True:
    eingabe = eingabe * 2
    print("Die Zahl wurde verdoppelt. Neuer Wert: {}".format(eingabe))
    weiter = eval(input("Soll weiter verdoppelt werden?(True/False): "))
    if weiter != True:
        break