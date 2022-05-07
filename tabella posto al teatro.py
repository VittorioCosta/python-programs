# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 05:18:34 2020

@author: slelenia
"""

import random

def main():
    t = [
       [10,10,10,10,10,10,10,10,10,10],
       [10,10,10,10,10,10,10,10,10,10],
       [10,10,10,10,10,10,10,10,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [10,10,20,20,20,20,20,20,10,10],
       [20,20,30,30,40,40,30,30,20,20],
       [20,30,30,40,50,50,40,30,30,20],
       [30,40,50,50,50,50,50,50,40,30],
       ]
    
    pos = getSit(t)
    return t
    
    
    
def getSit(t):
    print("do you wanna get a sit by price(P) or number(N)?")
    val = input()
    val=val.upper()
    while val!="P" and val!="N":
        print("do you wanna get a sit by price(P) or number(N)?")
        val = input()
    if val == "P": price(t)
    elif val == "N": number(t)
    

        
def number(t):
    for i in range(len(t)):
        print()
        for j in range(len(t[i])): print(t[i][j], end=" ")
    print()
    print("find a row")
    row = int(input())
    print("find a column")
    column = int(input())
    pos = t[row][column]
    if pos == 0:
        print("there sit is booked! find other sit")
        number(t)
    else:
        t[row][column] = 0
        print("you sit is ",row,column)
    return t

def price(t):
    print("which price do you want?")
    cost=int(input())
    for i in range(len(t)):
        for j in range(len(t[i])):
            if t[i][j]==cost:
                print("your sit is in",i,j)
                t[i][j]=0
                return t
    print("there aren't sit abouth that price")
    price(t)
    