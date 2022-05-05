string = "ox"
posizione = 0
prec = ""
stop = False
a =("x","o")

while not stop and  posizione < len(string):
    if string[posizione] in a and prec in a:
            print("contiene la sequenza")
            stop = True
    elif posizione + 1 == len(string):
        print("non contiene la sequenza")
    if string[posizione] == "x" or string[posizione]=="o":
        prec = string[posizione]
    posizione +=1

