import random
lista = []
for n in range(100):
    number = random.randint(1,9)
    lista.append(number)

for n in range(20):
    if n!=99 and lista[n]==lista[n+1] and lista[n]!=lista[n-1]: print("(", end="")
    if lista[n]==lista[n-1] and lista[n]!=lista[n+1]: print(lista[n], end="")
    else: print(lista[n], end=" ")
    if lista[n]==lista[n-1] and lista[n]!=lista[n+1]: print(")",end="")
print()
