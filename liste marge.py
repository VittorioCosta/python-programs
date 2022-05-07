# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 06:32:08 2020

@author: slelenia
"""


a = [1,2,3,4]
b = [5,6,7,8,9,10,11,12]

def marge(a,b):
    lista = []
    while len(a)<len(b):
        for i in range(len(a)):
            lista.append(a[i])
            lista.append(b[i])
        c = b[len(a):]
        for i in c:
            lista.append(i)
        return lista
            
            