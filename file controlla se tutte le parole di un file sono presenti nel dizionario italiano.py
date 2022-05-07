import os.path


def main():
    file = input("-> ")
    while not os.path.isfile(file):
        file = input("-> ")
    
    
    lista = words(file)
    lista = cutInteger(lista)
    lista = cutSymbol(lista)
    lista = ceck(lista)
    print(lista)
    
    
    
    
    
#return lista di tutte le parole splittate da tutti i simboli, compreso "un'abc"
def words(file):
    file = open(file,"r")
    lista=[]
    
    for line in file:
        line=line.split("'")
        lista.append(line)
        
    lista2 = []  
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            a = lista[i][j].split()
            for k in a: lista2.append(k)
    
    
    lista = []
    for i in range(len(lista2)):
        b = lista2[i]
        lista.append(i)
        
    
    
    
    file.close()
    return lista2
    


def cutInteger(lista):
    lista2 = []
    for word in lista:
        try: num=float(word)
        except ValueError: lista2.append(word)
    return lista2

def cutSymbol(lista):
    lista2 = []
    for word in lista:
        a = word
        a=a.strip(''',';.:()!?''')
        lista2.append(a)
    return(lista2)

def ceck(lista):
    cat = open("C:\\Users\\slelenia\\Desktop\\vitWork\\words.italian.txt","r")
    lista2=[]
    diz = []
    for line in cat:
        c = str(line)
        c = c.strip()
        diz.append(c)
    
    for word in lista:
        word = word.lower()
        if word not in diz and word not in lista2:
            lista2.append(word)
        
       
        
            
    return lista2
    
