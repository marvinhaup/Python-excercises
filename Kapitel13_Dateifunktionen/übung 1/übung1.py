# Aufnamhe von Gästen in einer Gästeliste, mit Hilfe einer Textdatei

def writeToFile():
    weiter = 'ja'
    while (weiter == 'ja'):
        weiter = 'nein'
        writeName = input("Vor- und Nachname des Gastes angeben:")
        fid.write(writeName+"\n")
        weiter = input("Soll ein weiterer Name ingelesen werden?(ja/nein): ")

try:
    fid = open('Gästeliste.txt','a')
    writeToFile()
except IOError:
    fid = open('Gästeliste.txt','w')
    writeToFile()
finally:
    fid.close()