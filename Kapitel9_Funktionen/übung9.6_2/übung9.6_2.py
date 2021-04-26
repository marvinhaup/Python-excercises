# Programm zum überprüfen von vorhandenen Benutzerkonten mit zugehörigem Passwort
# Prüft, ob Rückgabewert der aufgerufenen Funktion True ist und damit, ob die übergebenen Benutzerdaten korrekt sind.

import modules.module_checkuserexists
myfunc = modules.module_checkuserexists.istvorhanden

inputusername = input("Geben Sie den Benutzernamen ein:")
inputpassword = input("Geben Sie das zugehörige Passwort ein:")

checkifexists = myfunc(inputusername,inputpassword)

if checkifexists == True:
    print("Rückgabewert des Prüfmodules ist True")