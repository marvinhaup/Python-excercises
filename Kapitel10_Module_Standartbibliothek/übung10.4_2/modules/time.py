# Programm, dass die time bibliothek verwendet und eine strukturierte Rückgabe der Zeit erzeugt.

import time

def ReturnDateAndTime():
    return time.asctime( time.localtime(time.time()) )