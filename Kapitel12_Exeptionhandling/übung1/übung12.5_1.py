# Programm, das zwei vom Benutzer eingegebene Zahlen auf Bedingungen überprüft.

try:
    firstinput = int(input("Geben Sie ihre erste Zahl ein:"))
    secondinput = int(input("Geben Sie ihre zweite Zahl ein:"))
    print("Erste Zahl: {}, dividiert durch zweite Zahl: {}, ergibt: {}".format(firstinput,secondinput,firstinput
                                                                               /secondinput))
except ZeroDivisionError:
    print("Es darf nicht durch Null geteilt werden.")
except ValueError:
    print("Die Operanden müssen ganzzahlig und positiv sein")
except TypeError:
    print("Die Operanden müssen zahlen sein.")
else:
    print("Division erfolgreich.")
print("Tschau Kakao!")
