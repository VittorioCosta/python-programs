man = "X"


def main():
    counter = int(input("---> "))
    lista = ["_"]*counter
    for n in range (counter):
        if lista[counter//2]!= man: lista[counter//2] = man
        elif lista[0]!= man: lista[0] = man
        elif lista[counter-1]!= man: lista[counter-1] = man
        else:
            a = pos(lista)
            if lista[a]!= man: lista[a] = man
            elif lista[a+1]!= man: lista[a+1] = man
            elif lista[a-1]!= man: lista[a-1] = man
            elif lista[a+2]!= man: lista[a+2] = man
            elif lista[a-2]!= man: lista[a-2] = man
            else:
                for i in range(counter-1):
                    if lista[i]!= man: lista[i]=man
            
        print(lista)
    
    print(a)    
    



## cerco la ripetizione più lunga con la sua posizione finale


def lpl(run):
    count = 1
    massimo = 1
    p = 0
    for i in range(1,len(run)):
        if run[i] == run[i-1]:
            count +=1
            if count > massimo:
                massimo=count
                p = i
        if run[i] != run[i-1]: count = 1
        
    return (p,massimo)

## una volta riempito il centro cerco ed i due estremi,dsf una posizione 

def pos(lista):
    c = lpl(lista)
    a = c[1]-(c[0]-1)
    b = c[1]
    print(a,b,c)
    return (a+b)//2
        
    
    
    
main()






        
        
    


