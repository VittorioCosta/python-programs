
tab = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
    ]


table = []
rows = 5
columns = 3

for i in range(rows):
    row = [0]*columns
    table.append(row)


for i in range(rows):
    for j in range(columns):
        if table[i][j-1]==0: table[i][j]=1
        elif table[i][j-1]==1: table[i][j]=0
        elif table[i-1][columns]==0: table[i][j]=1
        elif table[i-1][columns]==1: table[i][j]=0

for i in range(rows):
    for j in range(columns):
        if i == 0 or i == rows-1: table[i][j]=1


for i in range(rows):
    for j in range(columns):
        if j==0 or j==2: table[i][j]=1

somma=0
for i in range(rows):
    for j in range(columns):
        somma += table[i][j]

for i in range(rows):
    print()
    for j in range(columns):
        print(table[i][j],end=" ")









