print('''ciao, inserisci un numero intero
compreso tra 1000 e 999999
per averlo restituito
in forma anglosassone\n''')

numero_utente = (input("inserisci numero qui----> "))
print("\n")


numero_utente = str(numero_utente)

parte_finale = numero_utente[-3:]
parte_iniziale = numero_utente[0:-3]

print(parte_iniziale + "," + parte_finale)

      


