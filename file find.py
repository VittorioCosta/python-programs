

argv = ["find.py", "p", "outP.txt", "bProva.py", "aProva.py"]



def  main():
    rat = argv[1]

    l = len(argv)
    lista = []
    nomi = []
    
    for i in range(l):
        i=[]*l
        lista.append(i)
        nomi.append(i)
    
    for i in range(2, len(argv)-1):
        file = open(argv[i],"r")
        nomi[i].append(argv[i])
        for line in file:
            if rat in line: lista[i].append(line)
        file.close()
    
    for i in range(2,len(nomi)):
        print(nomi[i],":\n")
        print(lista[i])

main()