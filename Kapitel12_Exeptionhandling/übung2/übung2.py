class UnEqualStringLengthError(Exception):
    def __init__(self,laenge):
        self.Length = laenge

try:
    mystr = str(input("Wort mit gerader Anzahl an Buchstaben angeben: "))
    mystrlen = len(mystr)
    if ((mystrlen % 2) != 0):
        raise UnEqualStringLengthError(mystrlen)
    else:
        middlevalue = int(mystrlen/2)
        newFirstWord = mystr[0:middlevalue]
        newSecondWord = mystr[middlevalue:]
        print("erste Häfte der Eingabe:{}\nZweite Hälfte der Eingabe:{}".format(newFirstWord,newSecondWord))
except UnEqualStringLengthError as ungeradeAnzahl:
    print("Die Anzahl an Buchstaben: {},ist nicht gerade".format(ungeradeAnzahl.Length))
print("Tschao kakao")
