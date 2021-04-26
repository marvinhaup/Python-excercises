# Programm um Objektprogrammierung zu testen

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

class SUV(Auto):
    """
    Erstellt ein Objekt SUV: abgeleitet von der Klasse Auto.
    """
    def __init__(self,herst,mod,bjhr,prs,allrd):
        """
        Initialisiert ein neues Object Auto

        Argumente:
        * Hersteller (string) : Hersteller des Gebrauchtwagens
        * Modell (string) : Modell des Gebrauchtwagens
        * Produktionsjahr (int) : Jahr der Produktion
        * Preis (int) : Angestrebter Verkaufspreis
        * Allradantrieb (bool) : Vorhandensein von Allradantrieb
        """
        Auto.__init__(self,herst,mod,bjhr,prs)
        self.__Allradantrieb = allrd

    def getAllradantrieb(self):
        """
        Gibt zurück, ob ein Allradantrieb vorhanden ist (true), oder nicht (false).
        """
        return self.__Allradantrieb

class Kombi(Auto):
    """
    Erstellt ein Objekt Kombi, abgeleitet von der Klasse Auto.
    """
    def __init__(self,herst,mod,bjhr,prs,kffrvol):
        """
        Initialisiert ein neues Object Auto

        Argumente:
        * Hersteller (string) : Hersteller des Gebrauchtwagens
        * Modell (string) : Modell des Gebrauchtwagens
        * Produktionsjahr (int) : Jahr der Produktion
        * Preis (int) : Angestrebter Verkaufspreis
        * Kofferraumvolumen (int) : Volumen des Kofferraumes
        """
        Auto.__init__(self, herst, mod, bjhr, prs)
        self.__Kofferraumvolumen = kffrvol

    def getKofferraumvolumen(self):
        """
        Gibt das Volumen des Kofferraumes zurück
        """
        return self.__Kofferraumvolumen



vwgolf = Auto("Vw","Golf",2010,5000)
renaultclio = Auto("Renault","Clio",2005,4000)
audia4 = Auto("Audi","A4",2006,4500)
MBenz = SUV("Marcedes-Benz","M-Klasse",2014,15000,True)
audiA4Avant = Kombi("Audi","A4-Avant",2010,10000,1500)
kombiListe = [audiA4Avant]
for kombi in kombiListe:
    print("Hersteller: {}, Modell: {}, Baujahr: {}, Preis: {}, Kofferraumvolumen: {}".format(kombi.getHersteller(), kombi.getModell(),
                                                                                             kombi.getProduktionsjahr(), kombi.getPreis(),
                                                                                             kombi.getKofferraumvolumen()))


"""
bestandsListe = [vwgolf,renaultclio,audia4]

for auto in bestandsListe:
    print('Hersteller: {}, Modell: {}, Baujahr: {}, Preis: {}'.format(auto.getHersteller(),auto.getModell(),auto.getProduktionsjahr(),auto.getPreis()))

neuerpreisvw = eval(input("\n\nGeben Sie einen neuen Preis für den Vw ein:"))
vwgolf.setPreis(neuerpreisvw)
print('Neuer Preis {}'.format(vwgolf.getPreis()))
"""
