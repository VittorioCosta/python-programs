a=['1','2','3','4','5','6','7','8','9']
s = "0000000000000000000000000000000000000000001"                    
inc = 0
trovato=False

while not trovato and inc < len(s):
    if s[inc] in a:
        print("num int")
        trovato = True
    elif inc + 1 == len(s):
        print("non trovato")
    inc += 1
    
