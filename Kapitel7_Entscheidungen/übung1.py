vwgolf = ["Volkswagen", "Golf", 2010, 5000]
mazda2 = ["mazda", "2", 2011, 4000]
audia4 = ["audi", "A4", 2006, 4500]
ListeallerAutos = [vwgolf, mazda2, audia4]
maxpreis = eval(input("Geben Sie ihre Obergrenze des Kaufpreises ein: "))
if maxpreis >= ListeallerAutos[0][3]:
    print(ListeallerAutos[0][0])
    print(ListeallerAutos[0][1])
    print(ListeallerAutos[0][2])
    print(ListeallerAutos[0][3],"\n")
if maxpreis >= ListeallerAutos[1][3]:
    print(ListeallerAutos[1])
if maxpreis >= ListeallerAutos[2][3]:
    print(ListeallerAutos[2])