fahrzeug1 = {"marke":"Peugoet","modell":"106","baujahr":2000,"Preis":4000}
print(fahrzeug1)
print(fahrzeug1["marke"])
fahrzeug1["marke"] = "porsche"
print(fahrzeug1)
del fahrzeug1["baujahr"]
print(fahrzeug1)
print(fahrzeug1.keys)
print(list(fahrzeug1.keys()))
print(sorted(fahrzeug1.keys()))