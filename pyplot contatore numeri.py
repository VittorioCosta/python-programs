from random import randint
from matplotlib import pyplot

uno = 0
due = 0
tre = 0
quattro = 0
cinque = 0
sei = 0
sette = 0
otto = 0
nove = 0


for ciao in range(1000):
    a = randint(1,999999)
    a = str(a)
    a = a[0]
    a = int(a)

    if a == 1: uno +=1
    elif a == 2: due +=1
    elif a == 3: tre +=1
    elif a == 4: quattro +=1
    elif a == 5: cinque +=1
    elif a == 6: sei +=1
    elif a == 7: sette +=1
    elif a == 8: otto +=1
    elif a == 9: nove +=1

pyplot.bar([1,2,3,4,5,6,7,8,9],
           [uno,due,tre,quattro,cinque,sei,sette,otto,nove])
pyplot.show()
