import sys

try:
    x = int(input("\nWert: "))
    print("Ergebnis: {}".format(4/x))
except ZeroDivisionError:
    print("Es darf nicht durch Null geteilt werden.")
except ValueError:
    print("Eingegebene Zahl muss ganzzahlig sein.")
except:
    print("Folgender Fehler ist aufgetreten: {}".format(sys.exc_info()[0]))
else:
    print("Die Berechnung wurde erfolgreich durchgeführt.")
print("Tschau Kakao!")
