from math import sqrt

num_str = "go"
lista = []
b = []
n = 0
a = 0
m = 0
c = 0
p = 0

while num_str != " ":               #creo lista
    num_str = str(input("input float ---> "))
    if num_str != " ":
        num = float(num_str)
        lista.append(num)

while n < len(lista):     #sommatoria di lista
    a = a + lista[n]
    n += 1

media = a/len(lista)

while m < len(lista):         # definisco xi*2 = b
    num2 = lista[m]**2
    b.append(num2)
    m += 1

while p < len(lista):     #sommatoria di b
    c = c + b[p]
    p += 1



s = sqrt((c - (1/len(lista))*((a)**2))/(len(lista) - 1))


print(" valori analizzati: %.d" % len(lista))
print("la media è %2.3f,   la deviazione standard è %2.3f" % (media, s))

    
