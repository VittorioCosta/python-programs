print('''Ciao, questo programma visualizza in mese corrispondente
la numero inserito\n''')
a = 1,2,3,4,5,6,7,8,9,10,11,12

while True:
    numero_utente = int(input("inserisci un numero da 1 a 12 ---> "))
    months = ('''Genuary  February March    April    May      June     July     Agust    SeptemberOctrober November December ''')

    if numero_utente == 1:
        print(months[0:9])
    elif numero_utente == 2:
        print(months[9:18])
    elif numero_utente == 3:
        print(months[18:27])
    elif numero_utente == 4:
        print(months[27:36])
    elif numero_utente == 5:
        print(months[36:45])
    elif numero_utente == 6:
        print(months[45:54])
    elif numero_utente == 7:
        print(months[54:63])
    elif numero_utente == 8:
        print(months[63:72])
    elif numero_utente == 9:
        print(months[72:81])
    elif numero_utente == 10:
        print(months[81:90])
    elif numero_utente == 11:
        print(months[90:99])
    elif numero_utente == 12:
        print(months[99:108])
