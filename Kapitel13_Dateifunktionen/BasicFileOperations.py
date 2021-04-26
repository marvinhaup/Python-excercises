# Programm zum Testen der Dateifunktion

print('Arbeiten mit der "Sortiment.txt"-Datei im Unterverzeichnis Dateien\.')
writeFolder = input("Dateipfad und Dateiname angeben:")
openMode = input("In welchem Modus soll die Datei geöffnet werden?(w,r,a):")
fid = open(writeFolder,openMode)

if (openMode == 'r'):
    content = fid.read()
    print(content)
else:
    brand = input("Hersteller des neuen Autos: ")
    modell = input("Modell dess neuen Autos: ")
    prodYear = input("Produktionsjahr des neuen Autos: ")
    price = input("Preis des neuen Autos: ")
    fid.write(brand+"\n")
    fid.write(modell+"\n")
    fid.write(prodYear+"\n")
    fid.write(price+"\n\n")
fid.close()