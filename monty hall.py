from random import *

count_stay = 0
count_change = 0



scelta = randint(1,3)
vincente = randint(1,3)
lista = [1,2,3]
lista1 = []

for n in range(1000):
    scelta = randint(1,3)
    vincente = randint(1,3)
    if scelta == 1 and vincente == 1: cas = randrange(2,3,1)
    elif scelta == 1 and vincente == 2 : cas = 3
    elif scelta == 1 and vincente == 3: cas = 2
    elif scelta == 2 and vincente == 1: cas = 3
    elif scelta == 2 and vincente == 2: cas = randrange(1,3,2)
    elif scelta == 2 and vincente == 3: cas = 1
    elif scelta == 3 and vincente == 1: cas = 2
    elif scelta == 3 and vincente == 2: cas = 1
    elif scelta == 3 and vincente == 3: cas = randrange(1,2,1)

    for n in range (1,4):
        if n != cas: lista1.append(n)


    if scelta == lista1[0]:scelta == lista[1]
    elif scelta == lista1[1]:scelta == lista[0]
    if scelta == vincente: count_change +=1

lista1 = []
for n in range(1000):
    scelta = randint(1,3)
    vincente = randint(1,3)
    if scelta == 1 and vincente == 1: cas = randrange(2,3,1)
    elif scelta == 1 and vincente == 2 : cas = 3
    elif scelta == 1 and vincente == 3: cas = 2
    elif scelta == 2 and vincente == 1: cas = 3
    elif scelta == 2 and vincente == 2: cas = randrange(1,3,2)
    elif scelta == 2 and vincente == 3: cas = 1
    elif scelta == 3 and vincente == 1: cas = 2
    elif scelta == 3 and vincente == 2: cas = 1
    elif scelta == 3 and vincente == 3: cas = randrange(1,2,1)

    if scelta == vincente: count_stay +=1

print("change: %2.d"% count_change)
print("stay: %6.d"% count_stay)

    
    


