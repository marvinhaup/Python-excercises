while True:
    eingabe = eval(input("Geben Sie eine zu verdoppelnde Zahl ein:"))
    print("Datentyp der Eingabe:",type(eingabe),"Doppelter Wert von",eingabe,", ist:",int(eingabe)*2)
    if input("Zum Fortfahren 'ja' eingeben:") != "ja":
        break