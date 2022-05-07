from sys import exit
print('''Ciao, questo programma calcola
il giorno in cui cade la Pasqua inserendo
l'anno desiderato\n''')
print('''   /\\
  /  \\
 /    \\
/      \\
--------
  "  "
  "  "
  "  "''')
while True:
    print("\n")
    y = int(input("inserisci l'anno o premi 0 per uscire ---> "))

    a = int(y % 19)     #   algoritmo
    b = int(y / 100)
    c = int(y % 100)
    d = int(b / 4)
    e = int(b % 4)
    g = int((8 * b + 13) / 25)
    h = int((19 * a + b - d - g + 15) % 30)
    j = int(c / 4)
    k = int(c % 4)
    m = int((a + 11 * h) / 319)
    r = int((2 * e + 2 * j - k - h + m + 32) % 7)
    n = int((h - m + r + 90) / 25)
    p = int((h - m + r + n + 19) % 32)

    if n == 1:
        month = ("Genuary")
    elif n == 2: month = ("February")
    elif n == 3: month = ("March")
    elif n == 4: month = ("April")
    elif n == 5: month = ("May")
    elif n == 6: month = ("June")
    elif n == 7: month = ("July")
    elif n == 8: month = ("Agoust")
    elif n == 9: month = ("September")
    elif n == 10: month = ("October")
    elif n == 11: month = ("November")
    elif n == 12: month = ("December")

    print("\n")

    if y >= 2021:
        print("La pasqua nell'anno %.d cadrà il %.d di %.s" % (y, p, month))
    elif y == 0:
        exit()
    else: print("La pasqua nell'anno %.d è caduta Domenica %.d di %-1.s" % (y, p, month))

    print(month)

