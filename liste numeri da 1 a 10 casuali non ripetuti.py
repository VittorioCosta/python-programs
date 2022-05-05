import random
lista = []
newlista = [1,2,3,4,5,6,7,8,9,10]

for n in range(10):
    top=len(newlista)-1
    if len(newlista)!=1:
        i = random.randint(1,top)
        
        lista.append(newlista[i])
        newlista.pop(i)
lista.append(newlista[0])       
for j in lista:
    print(j,end=" ")
print()
    
