audia4 = {"marke":"audi","modell":"A4","baujahr":2006,"preis":4500}
for inhalt in audia4:
    print(inhalt, audia4[inhalt])


count = 0
simplelist = ["eins","zwei","drei","vier","fünf","sechs"]
for inhalt in simplelist:
    print("Liste an der stelle",count + 1,"Listen-Inhalt:",inhalt)
    count += 1

# Noch verständlicher 

mydict = dict(schlüssel1="inhalt1",schlüssel2="inhalt2",schlüssel3="inhalt3",schlüssel4="inhalt4")
for var in mydict:
    print("Schlüsselbegriff:",var,"inhalt:",mydict[var])