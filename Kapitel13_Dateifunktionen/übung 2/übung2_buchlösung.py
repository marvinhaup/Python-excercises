# Lösung der übungsaufgabe laut des buches

fid = open('Gästeliste.txt','r')
myList = fid.readlines()
fid.close()

foundname = False
searchName = input("Welchen Gast möchten Sie löschen:")

for i in range(len(myList)):
    if (myList[i] == eingabe+'\n'):
        fid = open('Gästeliste.txt','w')
        myList = myList[:i] + myList[i+1:]
        for line in myList:
            fid.write(line)
        print(searchName, "wurde erfolgreich gelöscht")
        break

if not foundname:
    print(searchName, "ist nicht in der liste enthalten")