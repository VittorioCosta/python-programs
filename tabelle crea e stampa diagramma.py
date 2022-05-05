# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 05:22:26 2020

@author: slelenia
"""


## stampa grafici a barre positivi e negativi:



def main():
    table = inserDati()
    return stampaDiagramma(table)




def inserDati():
    tab=[
        [],
        []
        ]
    nome = ""
    valore = 0.0
    while nome!="Q":
        print("inserire nome")
        nome = input()
        if nome!="q" and nome!="Q": tab[0].append(nome)
        nome = nome.upper()
        if nome == "Q": return tab
        print("inserire valore")
        valore = float(input())
        
        tab[1].append(valore)

def stampaDiagramma(t):
    #cerco stringa più lunga
    a = strlng(t)+2
    negative = ceckNegative(t)
    if negative is False: printPositive(t,a) 
    elif negative is True: printNegative(t,a)
    return
    
def printNegative(t,a):
    #cerco il valore più grande in valore assoluto
    lista=[]
    for i in t[1]:
        lista.append(abs(i))
    m = max(lista)
    MAX=30 #lunghezza massima di un lato
    count = 0
    minimo=min(t[1])
    for i in t[0]:
        if len(i)==a-2: print(i,"  ",end="")
        elif len(i)//2==0: print(i," "*((a-len(i))//2),end="")
        elif len(i)//2!=0: print(i," "*((a-len(i))//2)," ",end="")
        numero = lista[count]
        numero = int(numero)
        sneg = t[1][count]+abs(minimo) #spazi da stampare in caso di numeri negativi
        if t[1][count]<0: print(" "*sneg,"-"*numero)
        elif t[1][count]>=0: print(" "*(abs(minimo)),"-"*numero)
        count+=1
        
    return    

        
def printPositive(t,a):
    MAX = 30 # lunghezza massima del grafico
    # cerco il valore più grande
    m = 0
    for j in t[1]:
        if j > m: m = j
        
    #stampo il diagramma
    count = 0
    for i in t[0]:
        if len(i)==a-2: print(i,"  ",end="")
        elif len(i)//2==0: print(i," "*((a-len(i))//2),end="")
        elif len(i)//2!=0: print(i," "*((a-len(i))//2)," ",end="")
        numero = (t[1][count]*MAX)//m
        numero = int(numero)
        print("-"*numero)

        count+=1
    return
    
    
        
def strlng(t):
    m = 0
    for i in t[0]:
        a = len(i)
        if a>m: m=a
    return m

def ceckNegative(t):
    ceck = False
    for i in t[1]:
        if i<0: 
            ceck=True
            break
    return ceck

main()




