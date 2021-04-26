def compformula(firstnumber,secondnumber):
    if firstnumber < secondnumber:
        for step in range(firstnumber,secondnumber+1,2):
            print(step)
    else:
        for step in range(firstnumber,secondnumber-1,-2):
            print(step)