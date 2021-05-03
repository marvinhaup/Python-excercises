# Programm zum löschen eines Teilnehmers der Gästeliste-Datei

searchName = input("Welcher Teilnehmer soll von der Liste entfernt werden?")
foundName = False

try:
    fid = open('Gästeliste.txt','r')
except FileNotFoundError:
    print("Die Datei konnte nicht gefunden werden, exit!")
    exit()

content = fid.readlines()
fid.close()
print(content)


for tup in content:
    if (tup == searchName):
        foundName = True

if not foundName:
    print("Der Name wurde nicht gefunden")
else:
    newList = []
    for tup in content:
        if not (tup == searchName):
            newList += tup
    print(content)
    print(newList)
    fid = open('Gästeliste.txt','w')
    for tup in newList:
        fid.write(tup + '\n')
    fid.close()