print('''
benvenuto,questo è un programma
realizzato da Vittorio
per calcolare il resto
''')

PRNNY_IN_DOLLARS = 100
PENNY_IN_QUARTER = 25
QUARTES_IN_DOLLAR = 4

money_input = float(input("quanti soldi hai inserito? "))
money_pay = float(input("quanto è il totale della spesa? "))

resto = money_input - money_pay
restoint = int(resto)
cent = resto % restoint
resto_in_cent = cent*100

if resto_in_cent < 25:
    a = resto_in_cent
elif resto_in_cent >= 25:
    a = int(resto_in_cent // 25)
    b = int(resto_in_cent % 25)

print("riceverai %.d dollari" % restoint)
print("riceverai %.d quarti di dollaro" % a)

if b != 0:
    print("riceverai %.d penny" % b)
    



