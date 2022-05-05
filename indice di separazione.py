# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 06:59:27 2020

@author: slelenia
"""

somma=1


def main():
    degree = int(input("DEGREE---> "))
    average = int(input("AVERAGE FRIENDS PER USER--->"))
    (reachalbePeoplePerUser(degree,average))
    return print("%.d peoples"% somma)
    
    
def reachalbePeoplePerUser(d,a):
    global somma
    somma_parte = a**d
    somma = somma + somma_parte
    if d == 1: return 
    reachalbePeoplePerUser(d-1,a)
    
    
main()