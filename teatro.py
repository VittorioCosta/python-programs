from math import tan
from math import atan
from math import sin
from math import asin
from math import sqrt
from math import cos

a = 24
a1 = 30
angolo_poltrone = 8
angolo_complementare = 90-angolo_poltrone

##calcola l'angolo di visuale di uno spettatore al cinema
# param distanza dallo schermo
# return angolo di visuale
#
def main():
    x = float(input("DISTANZA DALLO SCHERMO--->"))
    b = findb(x)
    c = latosup(b)
    beta = findbeta(a1,b,c,angolo_complementare)
    alpha = findalpha(a,c,beta)
    return print("%3.3f°"% alpha)





##calcola la linghezza del lato su cui poggiano le poltrone
# param distanza dallo schermo
# return lunghezza lato
#
def findb(x):
    b = x/sin(angolo_poltrone)
    return b

## ottiene il lato tra il punto di visone ed il vertice superiore dello schermo
# param b
# return lato superiore
#
def latosup(b):
    c = sqrt(a1**2+b**2-2*a1*b*cos(angolo_complementare))
    return c

def findbeta(a1,b,c,ang):
    p = (a1+b+c)/2
    s = sqrt(p*(p-a1)*(p-b)*(p-c))
    h = (2*s)/c
    beta = 90 - (ang/2)
    return beta

def findalpha(a,c,beta):
    b = sqrt(a**2+c**2-2*a*c*cos(beta))
    alpha = asin(sin(beta)/b)
    return alpha









main()
