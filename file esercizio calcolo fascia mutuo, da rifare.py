import os.path
from csv import reader




file = os.path.join("C:\\Users\\slelenia\\Desktop","deductions.csv")
file = open(file,"r")
newfile=open("C:\\Users\\slelenia\\Desktop\\output.txt","w")
cswReader = reader(file)  # legge il file riga per riga(x saltare una
                          # riga usare next(cswReader)   )

for row in cswReader:
    line=row
    print(line,file=newfile)
