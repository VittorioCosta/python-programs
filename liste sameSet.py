## verifica se tutti gli elementi di entrambe sono uguali
 # tralasciando i duplicati

def sameSet(a,b):
    ceck = []
    for i in a:
        if i not in b: ceck.append(i)
    for i in b:
        if i not in a: ceck.append(i)
    if len(ceck)==0: return True
        
