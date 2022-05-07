import os.path
def main():
    # ask file name and ceck if it s exists
    print("filename")
    file = "C:\\Users\\slelenia\\Desktop\\vitWork\\yob2019.txt"
    while not os.path.isfile(file):
        print("filename")
        file = input("-> ")
        
    # 0nome 1gen 2ricorrenze 3maschi 4femmine 5ricmaschi 6ricorfemmine
    lista = creaLista(file)
    lista = gender(lista)
    
    # 0nome 1gen 2ricorrenze
    rankAll100 = rankAll(lista)
    print(rankAll100)
    
    listaSeparati = files(lista)
    
    listaBolt = bolt(listaSeparati)
    print(listaBolt)
    
    
    
    
        
    
# inserisco i dati del file in una tabella
def creaLista(file):    
    lista = [[],[],[],[],[],[],[]]
    file = open(file,"r")
    for line in file:
        line=line.rstrip()
        line=line.split(",")
        line[2]=int(line[2])
        lista[0].append(line[0])
        lista[1].append(line[1])
        lista[2].append(line[2])
    file.close()
    
    for i in range(len(lista[2])):
        lista[2][i]=int(lista[2][i])
        
    return lista
    
# cerco i maschi e le femmine con le proprie ricorrenze
def gender(lista):
    for name in lista[0]:
        if lista[1]=="M":
            lista[3].append(lista[0])
            lista[5].append(lista[2])
        elif lista[1]=="F":
            lista[4].append(lista[0])
            lista[6].append(lista[2])
    return lista

# trovo i 100 nomi più diffusi
def rankAll(lista):
    listaRank = [[],[],[]]
    while len(listaRank[0])<100:
        maxValue=0
        pos = 0
        for i in range(len(lista[0])):
            if lista[2][i]>maxValue:
                maxValue=lista[2][i]
                pos = i
        listaRank[0].append(lista[0][pos])
        lista[0].pop(pos)
        listaRank[1].append(lista[1][pos])
        lista[1].pop(pos)
        listaRank[2].append(lista[2][pos])
        lista[2].pop(pos)
    return listaRank

# stampo due file col tutti i maschi e tutte le femmine
def files(lista):
    #riporto il valore di lista[2] in formato intero
    for i in range(len(lista[2])):
        lista[2][i]=str(lista[2][i])
    
    fileMen = open("C:\\Users\\slelenia\\Desktop\\vitWork\\men.txt","w")
    fileWomen = open("C:\\Users\\slelenia\\Desktop\\vitWork\\women.txt","w")
    listaSeparati = [[],[]]#la uso per trovare i nomi comuni nella funz seguente
    
    for i in range(len(lista[0])):
        if lista[1][i]=="M":
            print(lista[0][i]+" "+lista[2][i],file=fileMen)
            listaSeparati[0].append(lista[0][i])
        elif lista[1][i]=="F":
            print(lista[0][i]+" "+lista[2][i],file=fileWomen)
            listaSeparati[1].append(lista[0][i])
    fileMen.close()
    fileWomen.close()
    return listaSeparati

def bolt(listaSeparati):
    bolt = []
    for name in listaSeparati[0]:
        if name in listaSeparati[1]: bolt.append(name)
    return bolt
    
    
    
    

main()