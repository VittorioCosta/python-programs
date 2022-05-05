x = float(input("inserisci un numero "))
print("\n\n\n")
y = float(input("inserisci un secondo numero "))
print("\n\n\n")

somma = x+y
differenza = x-y 
prodotto = x*y
average = (x+y)/2

massimo = max(x,y)
minimo = min(x,y)

distanza = (massimo - minimo)

print("somma:       %-10.3f" % somma)
print("differenza:  %-10.3f" % differenza)
print("prodotto:    %-10.3f" % prodotto)
print("average:     %-10.3f" % average)
print("massimo:     %-10.3f" % massimo)
print("minimo:      %-10.3f" % minimo)
print("distanza:    %-10.3f" % distanza)
