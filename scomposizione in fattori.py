while True:
    print("\n")
    a = int(input("---> "))
    n = a
    lista = []
    count = 0
    lista_den =[]
    lista_fattori =[]
    c = 0


    for m in range(1, n+1):            #trovo i numeri primi 
        for p in range(1, m+1):
            if m >= p and m%p == 0: count += 1
        if count <= 2: lista.append(m)
        count = 0    

    if n in lista: print("%.d è un numero primo" % n)
    
    while n not in lista:
        while n != 1:
            for m in range(1, len(lista)): #trovo il più piccolo divisibile e mando tutto in while fino a 1
                if n >= lista[m] and n % lista[m] == 0: lista_den.append(lista[m])
            den = min(lista_den)
            n = n/den
            n= int(n)
            lista_fattori.append(den)
            lista_den = []
            
    

        print("la scomposizione in fattori del numero %.d è:" % a)


        for m in range(0, len(lista_fattori)):
            print(lista_fattori[m], end=" ")




        
        
