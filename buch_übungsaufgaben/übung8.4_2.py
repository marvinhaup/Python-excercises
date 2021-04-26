# Programm zur Ausgabe von Listen

mycitylist = ["Saarbrücken","St.Wendel","Hirstein","Namborn","München","Hamburg","Homburg"]

# Mit while-schleife

count = 0
#length = len(mycitylist)
while count < len(mycitylist):
    print("Stadt-Name:",mycitylist[count])
    count += 1

# Mit for-schleife

for tup in mycitylist:
    print("Stadt-Name:",tup)