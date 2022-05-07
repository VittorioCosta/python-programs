import os.path
os.chdir("C:\\Users\\slelenia\\Desktop\\vitWork")

def main():
    file = input("->" )
    while not os.path.isfile(file):
        print("invalid file name")
        a = os.listdir()
        print("the files in cwd are:",a)
        file = input("->" )

    lista = counter(file)
    return print(lista)


def counter(file):
    car ="abcdefghijklmnopqrstuvxywzABCDEFRGIJKLMNOPQRSTUVXYWZòàèéùì"
    caratteri = 0
    parole = 0
    righe = 0
    file=open(file,"r")
    
    for line in file:
        riga = line.split()
        parole += len(riga)
        righe += 1
        for i in riga:
            for j in i:
                if j in car: caratteri += 1
    
    
    
    lista = [caratteri,parole,righe]
    return lista
    
main()