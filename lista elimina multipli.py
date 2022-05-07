



def main():
    lista =[]
    for i in range(2,10001):
        lista.append(i)
    print(lista)
    
    
    j = 2
    
    while j <= 100:
        i = j
        while i <= 10000:
            i += j
            if i in lista: lista.remove(i)
        j += 1
    
    return print(lista)

main()