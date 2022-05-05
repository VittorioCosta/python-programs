B = 0.5
L = 2.0
T = 0.4
x = 0.5
n = 4

z = 0.0
passo = T/n
y = 0.5
lista_a = []

while z != -T + passo:
    yp = y
    y = abs((B/2)*(1-((2*x)/L)**2)
                   *(1-(z/T)**2))
    a = (1/2)*(y + yp)*passo
    lista_a.append(a)
    z = z - passo

a_triangolo = (y*passo)/2
a_tot = 0.0

for m in range(len(lista_a)):
    a_tot = a_tot + lista_a[m]

a_tot = a_tot + a_triangolo
a_tot = a_tot*2

print(a_tot)

    
    




