# Modultest der Random funktionen

import modules.randmodules

print("Welcher Würfel soll gewürfelt werden?")
decision = eval(input("1:Standart-würfel \n2:Würfel mit beliebig vielen Seiten\n:  "))
if decision == 1:
    erg = modules.randmodules.classicrand()
    erg = (erg * 10) % 7
    print("Zufallszahl: ",int(erg))

elif decision == 2:
    untergrenze = eval(input("Geben Sie eine Untergrenze ein:"))
    obergrenze = eval(input("Geben Sie eine Obergrenze ein:"))
    erg = modules.randmodules.randint(untergrenze,obergrenze)
    print("Zufallszahl lautet: ",erg)

# Erstellen einer beliebig langen Liste mit zufälligen Zahlen

mylist = []
length = eval(input("Wie lange soll ihre Zufallsliste sein: "))
untergrenze = eval(input("Geben Sie eine Untergrenze ein:"))
obergrenze = eval(input("Geben Sie eine Obergrenze ein:"))
count = 0
while count < length:
    erg = modules.randmodules.randint(untergrenze,obergrenze)
    mylist.append(erg)
    count += 1
for tup in mylist:
    print("Zufallsliste: ",tup)