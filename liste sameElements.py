## se contengono gli stessi elementi con gli stessi duplicati

def sameElements(a,b):
    if len(a)==len(b):
        
        for i in a:
            if i in b: b.remove(i)
    if len(b)==0: return True

