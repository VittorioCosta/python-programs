import math


pf = float(input("inserisci il fattore di potenza"))

R = 10.0
Vt = 120.0
P = 260.0


Vs = math.sqrt(((Vt+((2*R*P)/Vt))**2)+(
    ((2*R*P)/(pf*Vt))**2)*(1-(pf)**2))

print("il valore di Vs è %.3f Vrms" % (Vs))
