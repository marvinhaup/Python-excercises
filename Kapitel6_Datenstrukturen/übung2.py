buch1 = dict(titel="Algorithmen in C++",autor="Sedgewick",Artikelnummer=13,preis=20)
buch2 = dict(titel="C als erste Programmiersprache",autor="Joachim Goll",Artikelnummer=15,preis=30)
buch3 = dict(titel="Einstieg in Matlab",autor="Ulrich Stein",Artikelnummer=33,preis=10)

bookList = [buch1,buch2,buch3]
for book in bookList:
    for i in enumerate(book):
        print(i[1],":   ",book[i[1]])