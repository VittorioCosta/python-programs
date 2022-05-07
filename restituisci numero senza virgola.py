print('''ciao, inserisci un numero intero
compreso tra 10000 e 99999 in forma anglosassone
(10,000 oppure 99,999\n''')
numero_utente = str(input("inserisci numero qui----> "))
print("\n")

new_string = numero_utente.replace(",","")

new_string = int(new_string)

print(new_string)
