# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:32:01 2020

@author: slelenia
"""


#calcola il sussidio per figlio
#

famiglie = []
figli = []
redditi = []

def main():
    schedeFamiglie()
    sussidio()
    return
    
##aggiunge i dati alle liste, sentinella famiglia -1
# param cogome e nome, figli e reddito
# return liste aggiornate
#

def schedeFamiglie():
    global famiglie
    global figli
    global redditi
    famiglia = str(input("(end-1)FAMILY---> "))
    print(famiglia)
    if famiglia != "-1":
        famiglie.append(famiglia)
        figlio = int(input("NUMBER OF KIDS---> "))
        figli.append(figlio)
        reddito = float(input("INCOME---> "))
        redditi.append(reddito)    
        schedeFamiglie()
    return


def sussidio():
    for n in range(0, len(famiglie)):
        if redditi[n] >= 30000 and redditi[n]<40000 and figli[n] >=3: sussidio = figli[n]*1000
        elif redditi[n] >= 20000 and redditi[n]<30000 and figli[n] >=2: sussidio = figli[n]*1500
        elif redditi[n] < 20000 : sussidio = figli[n]*2000
        else: sussidio = 0.0
        print("The benefit of " + famiglie[n] + " family is %2.2f£ per month"% sussidio)
    return

main()