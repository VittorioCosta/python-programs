from random import randint
from matplotlib import pyplot

uno = 0
due = 0
tre = 0
quattro = 0
cinque = 0
sei = 0

for n in range(1000):
    a = randint(1,6)
    if a == 1: uno += 1
    elif a == 2: due += 1
    elif a == 3: tre += 1
    elif a == 4: quattro += 1
    elif a == 5: cinque += 1
    elif a == 6: sei += 1

pyplot.bar([1,2,3,4,5,6],[uno,due,tre,quattro,cinque,sei])

pyplot.show()
