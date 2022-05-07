# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 08:41:03 2020

@author: slelenia
"""
import random

## solitario bulgaro
def main():
    MAZZO = 45
    lista = creaLista(MAZZO)
    bulgaro(lista)
    print("\n")
    return print("IL SOLITARIO BULGARO è CONCLUSO!!!")

## crea la lista di lunghezza casuale, inserisce casualmente le carte.        
def creaLista(MAZZO):
    a = random.randint(1,MAZZO)
    count = MAZZO
    lista = [0]*a
    while count!=0:
        b = random.randint(0,(a-1))
        lista[b] +=1
        count -= 1
    rat = 0
    while rat in lista:
        lista.remove(rat)
    return lista

## crea un nuovo mazzo togliendo una carta ciascuno
#  return nove mazzi non ordinati di contenuro crescente da uno a nove
def bulgaro(lista):
    CECK = [1,2,3,4,5,6,7,8,9]
    cat = list(lista)
    while cat != CECK:
        a = 0
        for i in range(len(lista)):
            a += 1
            lista[i] -= 1
        lista.append(a)
        a=0
        rat=0
        
        while rat in lista:
            lista.remove(rat)
        print(lista)
                
        # CECK
        cat = list(lista)
        cat = sorted(cat)
        
    return
            
    

        

main()
    