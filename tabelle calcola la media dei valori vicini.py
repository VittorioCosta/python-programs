## calcola la media dei valori vicini di una matrice 5x5
## cambiando il valore di r e c si possono calcolare matrici di dimensioni differenti

values = [
    [14, 20, 21, 2, 8],
    [9, 15, 16, 22, 3],
    [4, 10, 11, 17, 23],
    [24, 5, 6, 12, 18],
    [19, 25, 1, 7, 13]
    ]
def neighborAverage(values, row, column):
    r =5 # righe matrice
    c =5 # colonne matrice
    r-=1
    c-=1
    if row==0 and column==0:
        average = values[0][1]+ values[1][1] + values[1][0]
    elif row==0 and column==c:
        average = values[0][c-1]+ values[1][c-1] + values[1][c]
    elif row==r and column==0:
        average = values[r-1][0]+ values[r-1][1] + values[r][1]
    elif row==r and column==c:
        average = values[r-1][c]+ values[r-1][c-1] + values[r][c-1]
    elif row==0 and column!=0 and column!=c:
        average=(values[0][column-1]+values[0][column+1]+
                 values[1][column-1]+values[1][column]+values[1][column+1])
    elif column==c and row!=0 and row!=r:
        average=(values[row-1][c]+values[row+1][c]+
                 values[row-1][c-1]+values[row][c-1]+values[row+1][c-1])
    elif row==r and column!=0 and column!=c:
        average=(values[r][column-1]+values[r][column+1]+
                 values[r-1][column-1]+values[r-1][column]+values[r-1][column+1])
    elif column==0 and row!=0 and row!=r:
        average=(values[row-1][0]+values[row+1][0]+
                 values[row-1][1]+values[row][1]+values[row+1][1])
    else:
        average=(values[row-1][column-1]+values[row-1][column]+values[row-1][column+1]+
                 values[row][column-1]+values[row][column+1]+
                 values[row+1][column-1]+values[row+1][column]+values[row+1][column+1])
        


        
    


    return average

print(neighborAverage(values,2,2))
