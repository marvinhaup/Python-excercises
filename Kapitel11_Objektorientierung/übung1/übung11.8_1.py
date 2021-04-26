# Programm zur Erstellung der Wohnungsverwaltung eines Ferienwohnungsvermieters

class Wohnung:
    """
    Erstellt ein Objekt der Klasse Wohnung.
    """
    anzahl = 0
    def __init__(self,wohnungsName,Standort,anzahlBetten,preisProuebernachtung):
        """
        Initialisiert ein neues Objekt Wohnung.

        Argumente:
        * Wohnungsname (string): der Name der Wohnung
        * Standort (string): genauer Standort der Wohnung
        * Anzahlbetten (int): Anzahl der Betten in der Wohnung
        * Preisproübernachtung (int): Preis der pro Übernachtung gezahlt wird
        """
        self.__Wohnungsname = wohnungsName
        self.__Standort = Standort
        self.__Anzahlbetten = anzahlBetten
        self.__Preisprouebernachtung = preisProuebernachtung

    def getWohnungsname(self):
        """
        Gibt den Wohnungsnamen des Objektes zurück
        """
        return self.__Wohnungsname

    def getStandort(self):
        """
        Gibt den Standort des Objektes zurück
        """
        return self.__Standort

    def getAnzahlBetten(self):
        """
        Gibt die Anzahl der Betten zurück
        """
        return self.__Anzahlbetten

    def getPreisproübernachtung(self):
        """
        Gibt den Preis pro Übernachtung zurück
        """
        return self.__Preisprouebernachtung

    def setPreis(self,preis_neu):
        """
        Legt einen neuen Preis fest, der pro Nacht gezahlt werden soll.
        Darf nicht negativ sein.
        """
        bestaetigung = "nein"
        print("Soll alter preis von {}: {}, zu neuem Preis: {}, abgeändert werden?".format(self.__Wohnungsname,self.__Preisprouebernachtung,preis_neu))
        bestaetigung = input("ja/nein : ")
        if bestaetigung == "ja":
            self.__Preisprouebernachtung = preis_neu

# Hauptprogramm

elfenbeinturm = Wohnung("Elfenbeinturm","Auf der Kuppe",1,300)
strandhaus = Wohnung("Haus am Strand","Zum Strand 3",5,250)
landhaus = Wohnung("Haus auf dem Lande","Zur Landstraße 5",6,200)
wohnungsListe = [elfenbeinturm,strandhaus,landhaus]

# Formatierte Ausgabe der wohnungsListe
for wohnung in wohnungsListe:
    print("Name: {}, Adresse: {}, Betten: {}, Preis: {}".format(wohnung.getWohnungsname(),wohnung.getStandort(),wohnung.getAnzahlBetten(),wohnung.getPreisproübernachtung()))

# Ändern der Wonungspreise

elfenbeinturm.setPreis(400)
strandhaus.setPreis(500)
landhaus.setPreis(600)

# Formatierte Ausgabe der wohnungsListe
for wohnung in wohnungsListe:
    print("Name: {}, Adresse: {}, Betten: {}, Preis: {}".format(wohnung.getWohnungsname(),wohnung.getStandort(),wohnung.getAnzahlBetten(),wohnung.getPreisproübernachtung()))
