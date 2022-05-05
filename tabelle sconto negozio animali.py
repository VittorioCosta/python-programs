# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 06:22:10 2020

@author: slelenia
"""
## se il cliente acquista un pet econ almeno 5 altri articoli
#  applica uno sconto su tutti gli articoli escuso pet

def main():
    tab = creaMat()
    price = sum(tab[0])
    print("PRICE WAS  %.2f"% price)
    return reduction(price,tab)
    
    
    
def creaMat():
    tab = [
        [],
        []
        ]
    val = 0
    while val != -1:
        val=float(input("price---> "))
        
        if val!=-1:
            pet = input("PET? (Y/N)")
            pet=pet.upper()
            tab[1].append(pet)
            tab[0].append(val)
    
    return tab

def reduction(price,tab):
    ypos=0
    for i in tab[1]:
        y=False
        ypos+=1
        if i=="Y":
            y=not y
            ypos-=1
            
    if "Y"  in tab[1] and len(tab[0])>5 :
        price = price - tab[0][ypos]
        price = price-((price*20)/100)
        price = price +  tab[0][ypos]
    
    
    return print("NEW PRICE %.2F"% price)
        
       
            