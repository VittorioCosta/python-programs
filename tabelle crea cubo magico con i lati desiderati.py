


def main():
    n = int(input("inserire un numero intero dispari---> "))
    while n%2!=1:
        n= int(input("inserire un numero intero dispari capra! ---> "))
    table=cuboMagico(n)


def cuboMagico(n):
    # crea matrice
    table = []
    for i in range(n):
        row = [0]*n
        table.append(row)
    # inserisce i valori
    riga = n-1
    colonna = n//2
    for k in range(1, n*n+1):
        table[riga][colonna] = k
        riga += 1
        colonna += 1
        riga1 = riga
        colonna1 = colonna
        if riga == n: riga = 0
        if colonna == n: colonna = 0
        if table[riga][colonna]!=0:
            riga = riga1
            colonna = colonna1
            riga -= 1


    print(table)
            
        


    
