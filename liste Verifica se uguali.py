## verifica se due liste contengono gli stessi elementi
## nello stesso ordine

def equals(a,b):
    if len(a)==len(b):
        for i in range(len(a)):
            if a[i]!=b[i]: return
        return True
    return

    
    
