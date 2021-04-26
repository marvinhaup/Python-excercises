# Programm zum bewerten der Rechenkenntnisse mit notenausgabe
Punkte = 0
if eval(input("Geben Sie das Ergebnis der Addition 1+1 ein: ")) == 2:
    print("Die Eingabe ist Korrekt")
    Punkte +=1
if eval(input("Wie lautet das Ergebnis der Subtraktion 99-37: ")) == 62:
    print("Die Eingabe ist Korrekt")
    Punkte +=1
if eval(input("Wie lautet das Ergebnis der Multiplikation 4x6: ")) == 24:
    print("Die Eingabe ist Korrekt")
    Punkte +=1


if Punkte > 2 and Punkte < 4:
    print("Super! Alle Aufgaben richtig gelöst.")
elif Punkte > 1:
    print("Gute Leistung.")
elif Punkte > 0:
    print("Viele Fehler, weitere übung erforderlich.")
else:
    print("Dringend Nachhilfe benötigt.")