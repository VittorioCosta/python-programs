# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 19:42:44 2020

@author: slelenia
"""
prima = ""
l = 0
count = -1
new = ""


def main():
    global l
    word = str(input("word to reverse---> "))
    l = len(word)
    new = reverse(word)
    if word == new: return print("palindromo")
    elif word != new: return print("non palindromo")

def reverse(w):
    global count
    global new
    global prima
    prima = w[0]
    new = new + w[count]
    count -= 1
    if len(new) != l: reverse(w)
    
    return new

main()