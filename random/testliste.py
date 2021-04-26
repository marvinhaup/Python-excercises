mylist = [3,234,32,44,234,645]
print(mylist)
for inhalt in enumerate(mylist):
    mylist[inhalt[0]] = inhalt[1] * 2
print(mylist)