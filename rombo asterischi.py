while True:
    l = int(input("side number ---> "))
    a = " "
    b = "*"
    lista = []
    count = 1


    for n in range(1, l + 1):
            code = a * (l - n) + (b * count) + "\n"
            lista.append(code)
            count += 2
    
    count -= 2
    for n in range(1, l):
            count -= 2
            code2 = (a * n) + (b * count) + "\n"
            lista.append(code2)

    for n in range(0, len(lista)):
            print(lista[n])
            
