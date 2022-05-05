n = 5
lista = []
count = 0
#trovo i numeri primi 

for m in range(1, n+1):
    for p in range(1, m+1):
        if m >= p and m%p == 0: count += 1
    if count <= 2: lista.append(m)
    count = 0    
        

