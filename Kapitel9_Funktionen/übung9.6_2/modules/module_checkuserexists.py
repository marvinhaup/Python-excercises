# Modul, das eine Liste mit Tupeln der existierenden Nutzern enthält.
# Prüft, ob die übergebene Kombination von Benutzername und Passwort in der Tupelliste vorhanden ist.
# Gibt bei Aufruf der Funktion "istvorhanden" entweder True oder False zurück

user1tup = "user1","password1"
user2tup = "user2","password2"
user3tup = "user3","password3"

existinguserstuples = [user1tup,user2tup,user3tup]
print(existinguserstuples)

def istvorhanden(username,password):
    for usertup in existinguserstuples:
        # print(usertup)
        if usertup[0] == username and usertup[1] == password:
            print("Suche Erfolgreich. Benutzerkombination gefunden!")
            return True
    print("Keine entsprechende Benutzerkombination gefunden.")    
    return False