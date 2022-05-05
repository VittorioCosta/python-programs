# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 04:34:42 2020

@author: Vittorio
"""

## operazioni con liste
#
#

lista = [1,2,3,4,5,6,7,8,9,10]
l = list(lista)
print(l)

def main():
    l = list(lista)
    a = swappa(lista)
    b = slideDx(lista)
    c = zeroPari(lista)
    d = sostBigAdiac(lista)
    e = eliminaCentro(lista)
    f = spostaPari(lista)
    g = secondoMaggiore(lista)
    h = crescente(lista)
    i = adiacDupli(lista)
    j = dupli(lista)
    print(a,b,c,d,e,f,g,h,i,j)
    return()

## scambia il primo e l' ultimo elemento della lista
def swappa(l):
    var = l[0]
    l[0] = l[-1]
    l[-1] = var
    return l

## inserisce l'ultimo elemento al posto del primo
def slideDx(l):
    var = l[-1]
    l.pop(-1)
    l.insert(0, var)
    return l

## sostituisce con zero tutti gli elementi pari
def zeroPari(l):
        for i in range(len(l)):
            if l[i]!=0:
                if l[i]%2==0:
                    l[i]=0
        return l

## sostituisce il numero con il numero più grane adiacente
def sostBigAdiac(l):
    for i in range(1,len(l)-1):
        if l[i-1]>l[i]: l[i]=l[i-1]
        if l[i+1]>l[i]: l[i]=l[i+1]
    return l

## elimina elemento/i al centro
def eliminaCentro(l):
    a = int((len(l)/2)-1)
    b = int(a+2)
    if len(l)%2!=0: l.pop(len(l)//2)
    elif len(l)%2==0: l[a:b]=[]
    return l

## sposta tutti i pari all'inizio della lista preservandone l'ordine
def spostaPari(l):
    new=0
    i = 0
    while i < len(l):
        if l[i]%2==0 and l[i]!=0 and l[i]!=1:
            l.insert(new,l[i])
            i +=1
            l.pop(i)
            new += 1
        i += 1
    return l

## restituisce il secondo valore maggiore della lista
def secondoMaggiore(l):
    primo = 0
    secondo = 0
    for n in range(len(l)):
        if l[n]>primo: primo = l[n]
    for n in range(len(l)):
        if l[n]>secondo and l[n]<primo: secondo = l[n]
    return secondo
        
## restituisce true se la lista è ordinata
def crescente(l):
    for n in range(1, len(l)):
        if l[n] <= l[n-1]: return
    return True
        
## se la lista contiene 2 elementi adiacenti duplicati restituisce true
def adiacDupli(l):
    for n in range(1, len(l)):
        if l[n] == l[n-1]: return True
    
## True se contiene due elementi duplicati
def dupli(l):
    for i in range(len(l)):
        a = l[i]
        count = 0
        for j in l:
            if a == j: count +=1
    if count > 1 : return True

main()
    
    

    



