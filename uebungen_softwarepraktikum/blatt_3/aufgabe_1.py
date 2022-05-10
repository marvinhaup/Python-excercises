def fib(wdh, count, vorletzter, letzter):
    if (wdh < 1): # Rekursionsanker, Ende der Wiederholungen
        print("Rekursionsende erreicht.")
        return
    else: 
        if (count < 3): # Ausgabe 1, solange unter 3 Wiederholungen
            print(count,". Fibonacci-Zahl: 1")
            tmp = letzter + vorletzter
            fib(wdh-1, count+1, vorletzter, letzter)
        else: # Falls Wiederholungen(count) größer 3
            tmp = letzter + vorletzter
            print(count,". Fibonacci-Zahl: ",tmp)
            fib(wdh-1, count+1, letzter, tmp)

def fibonacci(wdh):
    fib(wdh, 1, 1, 1)

fibonacci(10)