# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 04:32:41 2020

@author: slelenia
"""
Maiuscole = "QWERTYUIOPLKJHGFDSAZXCVBNM"
Minuscole = "qwertyuioplkjhgfdsazxcvbnm"
maiuscole_ceck = ""
minuscole_ceck = ""
Cifre = "1234567890"
cifre_ceck = ""

passw = str(input("PASS---> "))

while len(passw)<8:
    passw = str(input("INSERT A VALID PASS---> "))

for n in range(0,len(passw)):
    if passw[n] in Maiuscole: maiuscole_ceck += passw[n]
for n in range(0,len(passw)):
    if passw[n] in Minuscole: minuscole_ceck+= passw[n]
for n in range(0,len(passw)):
    if passw[n] in Cifre: cifre_ceck += passw[n]

while len(minuscole_ceck)==0 or len(maiuscole_ceck) == 0 or len(cifre_ceck)==0:
    passw = str(input("INSERT A VALID PASS---> "))
    for n in range(0,len(passw)):
        if passw[n] in Maiuscole: maiuscole_ceck+= passw[n]
    for n in range(0,len(passw)):
        if passw[n] in Minuscole: minuscole_ceck+= passw[n]
    for n in range(0,len(passw)):
        if passw[n] in Cifre: cifre_ceck += passw[n]









    


