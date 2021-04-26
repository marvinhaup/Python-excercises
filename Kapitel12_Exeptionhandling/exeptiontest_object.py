class Obj:
    wert = 4

try:
    object = Obj()
    x = int(input("Wert: "))
    print("Ergebnis: {}".format(Obj.wert/x))
except ZeroDivisionError:
    print("Es darf nicht durch Null geteilt werden.")
else:
    print("Die Berechnung wurde erfolgreich durchgeführt.")
finally:
    del object
    print("Objekt zerstört.")

print("Tschau Kakao!")

