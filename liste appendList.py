# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 06:32:08 2020

@author: slelenia
"""


a = [1,2,3,4]
b = [5,6,7,8,9,10,11,12]

def appendList(a,b):
    lista = []
    for i in a:
        lista.append(i)
    for j in b:
        lista.append(j)
    return lista
            