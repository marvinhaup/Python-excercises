# Hello-World ohne zwingende Übergabe von Parametern
# Standartparameter werden durch die Funktion selbst bestimmt, falls keine übergeben werden.

def hello_world(name="unknown",age="unknown",home="unknown"):
    print("Hello World!") 
    print("My name is:",name)
    print("i am:",age,"years old")
    print("and i live in:",home)
inputname = input("Geben Sie ihren Namen ein:")
inputage = input("Geben Sie ihr Alter ein:")
inputlocation = input("Geben Sie ihren Wohnort ein:")
hello_world()