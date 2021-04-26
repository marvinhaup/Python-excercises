# Programm zur Ausgabe der Quadratzahlen von 1 bis 10

# Mit einer while-Schleife
print("while-schleife:")
count = 1
while count <= 10:
    print("Das Quadrat von",count,", ist :",count*count)
    count += 1

# Mit einer for-Schleife
print("for-schleife")
for wert in range(1,11,1):
    print("Das Quadrat von",wert,",ist:",wert*wert)