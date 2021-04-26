mylist = [10,200,1,40,30000,0,4,10]

wert = eval(input("Welcher Wert soll dividiert werden?"))

for tup in mylist:
    if tup == 0:
        print("Fehler! Zahlen dürfen nicht durch Null geteilt werden.")
        continue 
    print(wert/tup)