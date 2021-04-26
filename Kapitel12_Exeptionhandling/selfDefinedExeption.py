class OutOfRangeError(Exception):
    def __init__(self,wert):
        self.Wert = wert

try:
    x = int(input("Geben Sie eine Zahl zwischen 10 und 20 ein: "))
    if x > 20 or x < 10:
        raise OutOfRangeError(x)
    print("Das Ergebnis von 4 durch {}, ist: {}".format(x,4/x))
except OutOfRangeError as fehler:
    print("Die Zahl: {} liegt nicht zwischen 10 und 20".format(fehler.Wert))
except ValueError:
    print("Eingegebene Zahl muss ganzzahlig sein.")

print("Tschau Kakao!")

