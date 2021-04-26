maxcount = 10

count = 0
simplelist = ["eins","zwei","drei","vier","fünf","sechs"]
while count < len(simplelist):
    print("Listen-Durchlauf Nummer: ", count+1,"Listen-Inhalt:", simplelist[count])
    count += 1

count = 0
mytupel = "eins","zwei","drei","vier","fünf","sechs"
while count < len(mytupel):
    print("Tupel-Durchlauf Nummer: ", count+1, "Tupel-Inhalt:",mytupel[count])
    count += 1

# Kein Zugriff auf Dictionary mit while-Schleife möglich, da Index nur mit Indexnamen abfragbar ist.

#count = 0
#mydict = {eins,zwei,drei,vier,fünf,sechs}
#while count < len(mydict):
#    print("Dictionary-Durchlauf Nummmer",count+1,", dict-Inhalt: ", mydict[])     