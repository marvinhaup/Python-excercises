import random

classicrand = random.random()
print("Standard-randomgenerator Wertebereich 0.0 bis 1.0:  ",rand1)

untergrenze1 = eval(input("Geben Sie eine Untergrenze ein:"))
obergrenze1 = eval(input("Geben Sie eine Obergrenze ein:"))
rand2 = float(random.randrange(untergrenze1,obergrenze1))
print("Zufallszahl innerhalb der Schranken:",untergrenze1,"und Obergrenze:",obergrenze1,"lautet: ",rand2)

untergrenze2 = eval(input("Geben Sie eine Untergrenze ein:"))
obergrenze2 = eval(input("Geben Sie eine Obergrenze ein:"))
rand3 = random.randint(untergrenze2,obergrenze2)
print("Zufalls-int innerhalb der Schranken:",untergrenze2,"und Oberschranke:",obergrenze2,"lautet:",rand3)