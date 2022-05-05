# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 05:39:42 2020

@author: slelenia
"""
## restituisce una lista ordinala da due liste ordinate
#  tenendo traccia delle due liste ordinate

a = [1,2,4,4,8,9,10,10,15,19]
b = [3,3,5,6,7,7,11]

def margeSorted(a,b):
    c = []
    
    while len(a)!=0 and len(b)!=0:
        if a[0]<=b[0]:
            c.append(a[0])
            a.pop(0)
        elif b[0]<a[0]:
            c.append(b[0])
            b.pop(0)
        
# se una lista è vuota incolla nella nuova il contenuto dell'altra
        if len(a)==0:
            for i in b:
                c.append(i)
            b = []
        elif len(b)==0:
            for j in a:
                c.append(j)
            a = []
    return c