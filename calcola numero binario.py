num = int(input("inserisci un numero intero "))
lista = []
r = 1


while num != 0:
    r = num % 2
    num = num//2
    lista.append(r)

range_ = len(lista)-1

for n in range(range_, -1, -1):
    print(lista[n])
