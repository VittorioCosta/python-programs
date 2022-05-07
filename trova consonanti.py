a = "harry"
vocali = ("a", "e", "i", "o", "u", "y")

val_ = ""
val_successivo = ""
val_precedente = ""
count = 0
n = 0
lenght = len(a)
while n < len(a):
    val = a[n]
    if n < lenght - 1: val_successivo = a[n+1]
    if val in vocali and val_successivo not in vocali:
        count +=1
    if n != 0:
        val_precedente = a[n-1]
        if (val not in vocali) and (val_precedente==" "):
            count +=1
    n +=1
        
