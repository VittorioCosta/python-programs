import math



f = float(input("inserisci il calore di f in Hz "))
print("\n")

c_min = float(input("inserisci il calore di Cmin in pF "))
print("\n")

c_max = float(input("inserisci il calore di Cmax in pF "))
print("\n")

c = math.sqrt(c_min*c_max)

l = ((((2*math.pi)/f)**2)/c)

f_min = (2*math.pi)/math.sqrt(l*c_min)
f_max = (2*math.pi)/math.sqrt(l*c_max)


print("\n\n")
print("l'induttanza L vale %.3f " % l)
print("il valore di fmin é %3.3f  il valore di fmax é %6.3f" % (f_min, f_max))



