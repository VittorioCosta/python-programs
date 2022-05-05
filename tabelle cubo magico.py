# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:11:14 2020

@author: slelenia
"""


## questo programma verifica se un quadrato è magico
#  non riempio la tabella inserendo valori ma con un ciclo casuale di tutti 
#  i valori da 1 a 16. nel caso si vuole analizzare la tab magica cambiare con tab2 in main
#



import random

CECK1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
rows = 4
columns = 4
tab2=[[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]

def main():
    tab = creaTab()
    tab = riempiTab(tab)
    return ceckMagico(tab)   # cambaire qui con tab2 per il ceck della lista magica
    


def creaTab():
    tab = []
    for i in range(rows):
        row = [0]*columns
        tab.append(row)
    return tab

def riempiTab(tab):
    lista = list(CECK1)
    for i in range(rows):
        for j in range(columns):
            k = random.randint(0,len(lista)-1)
            tab[i][j]=lista[k]
            lista.pop(k)
            
    return tab
        
def ceckMagico(tab):
        lista=[]
        for i in range(rows):
            for j in range(columns):
                lista.append(tab[i][j])
        lista = sorted(lista)
        if lista == CECK1: count = True
# cerco il valore della somma della prima riga, da usare come riferimento
        a = 0
        for i in range(columns):
            a+=tab[0][i]
        
# controlla se ogni riga è uguale al riferimento
        righe = True
        for i in range(1, rows):
            b=0
            for j in range(columns):
                b = b + tab[i][j]
            if b != a: righe = False

# controlla colonne
        colonne = True
        for i in range(columns):
            b = 0
            for j in range(rows):
                b+=tab[i][j]
            if b != a: colonne = False
        
# controlla diagonali
        one = uno(tab)
        two = due(tab)
        three = tre(tab)
        four = quattro(tab)
        diagonali = True
        if one!=two or one!=three or one!=four: diagonali==False
        
            
# fine
        fine = True
        if count!=True or righe!=True or colonne!=True or diagonali!=True: fine=False
        return print(fine)
            
            
def uno(tab):
    righe = 0
    colonne = 0
    somma = 0
    for i in range(columns):
        somma += tab[righe][colonne]
        righe+=1
        colonne+=1
    return somma

def due(tab):
    righe = 0
    colonne = 3
    somma = 0
    for i in range(columns):
        somma += tab[righe][colonne]
        righe+=1
        colonne-=1
    return somma

def tre(tab):
    righe = 3
    colonne = 0
    somma = 0
    for i in range(columns):
        somma += tab[righe][colonne]
        righe-=1
        colonne+=1
    return somma

def quattro(tab):
    righe = 3
    colonne = 3
    somma = 0
    for i in range(columns):
        somma += tab[righe][colonne]
        righe-=1
        colonne-=1
    return somma
            
    
    
        
                  
            
            
                
        
        
        
        
        
main()
        

    




