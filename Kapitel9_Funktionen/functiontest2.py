# Funktion zur Ausgabe von Personendaten
# Bei Aufruf der Funktion kann auf die variablen in der definierten Funktion zugegriffen werden.

def personendaten(name="unknown",age="unknown",location="unknown"):
    print("Name der Person:",name)
    print("Alter der Person:",age)
    print("Ort an dem sich die Person befindet:",location)

personendaten(location="Bielefeld")