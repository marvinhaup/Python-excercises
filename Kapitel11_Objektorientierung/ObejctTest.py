class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler.
    """
    anzahl = 0
    def __init__(self,herst,mod,bjhr,prs):
        """
        Initialisiert ein neues Object Auto

        Argumente:
        * Hersteller (string) : Hersteller des Gebrauchtwagens
        * Modell (string) : Modell des Gebrauchtwagens
        * Produktionsjahr (int) : Jahr der Produktion
        * Preis (int) : Angestrebter Verkaufspreis
        """

        self.__Hersteller = herst
        self.__Modell = mod
        self.__Produktionsjahr = bjhr
        self.__Preis = prs
        Auto.anzahl += 1

    def __del__(self):
        """
        Löscht ein Objekt der Klasse Auto.
        """
        Auto.anzahl -= 1

    def getHersteller(self):
        """
        Gibt den Hersteller des Autos zurück
        """
        return self.__Hersteller

    def getModell(self):
        """
        Gibt das Modell des Autos zurück
        """
        return self.__Modell

    def getProduktionsjahr(self):
        """
        Gibt das Produktionsjar des Autos zurück
        """
        return self.__Produktionsjahr

    def getPreis(self):
        """
        Gibt den Hersteller des Autos zurück
        """
        return self.__Preis

    def setPreis(self,preis_neu):
        """
        Ändert den Preis des Autos
        """
        if abs(self.__Preis - preis_neu) < self.__Preis * 0.05:
            self.__Preis = preis_neu
        else:
            print("Die Abweichung des neuen Preises zum alten Preis ist sehr hoch.")
            bestaetigung = input("Soll der neue Preis trotzdem: {} sein? (ja/nein): ".format((preis_neu)))
            if bestaetigung == "ja":
                self.__Preis = preis_neu