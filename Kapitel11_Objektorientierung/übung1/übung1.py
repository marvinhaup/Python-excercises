# Programm zum Erstellen von Objekten der Klase Wohnung

class Wohnung():
    """
    Erstellt ein Objekt der Klasse Wohnung
    """
    def __init__(self,ort,betten,pÜber):
        """
        Initialisiert ein neues Objekt Wohnung

        Argumente:
        * Standort (string)             : Standort der Wohnung
        * Bettenanzahl (int)            : Anzahl der Betten in der Wohnung
        * Übernachtungspreis (float)    : Preis pro Übernachtung
        """

        self.__Standort = ort
        self.__Bettenanzahl = betten
        self.__Übernachtungspreis = pÜber

    def getStandort(self):
        """
        Liefert den Standort der Wohnung zurück
        """
        return self.__Standort

    def getBettenanzahl(self):
        """
        Liefert Bettenanzahl zurück
        """
        return self.__Bettenanzahl

    def getÜbernachtungsspreis(self):
        """
        Liefert Übernachtungspreis zurück
        """
        return self.__Übernachtungspreis

    def setÜbernachtungspreis(self,neuerPreis):
        """
        Legt neuen Preis für die Übernachtung fest
        """
        self.__Übernachtungspreis = neuerPreis

hausAmSee = Wohnung("AmTümpel1",2,99.99)
schlossAufBerg = Wohnung("AufDemBerg",100,999)
plattenBau = Wohnung("Platte42",200,69.69)
myList = [hausAmSee,schlossAufBerg,plattenBau]

for tup in myList:
    print(tup.getStandort(),tup.getBettenanzahl(),tup.getÜbernachtungsspreis())