valore_soglia = float(input("valore di soglia---> "))

vendere = 0

while vendere == 0:
    a = float(input("valore azioni---> "))
    if a >= valore_soglia:
        vendere = 1

if vendere == 1: print ("vendere azioni")
    
