weiter = "ja"
while weiter == "ja":
    zahl = eval(input("Zu verdoppelnde Zahl eingeben: "))
    print("Das Quadrat von",zahl,"ist: ",zahl * zahl)
    weiter = input("Möchten Sie fortfahren? ja/irgendwas : ")