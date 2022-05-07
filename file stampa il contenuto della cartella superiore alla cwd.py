import os

cwd = os.getcwd()

c=""
count=len(cwd)
while c != "\\":
    count -= 1
    c = cwd[count]
    

cwd1 = cwd[:count]
cwd2 = ""

for c in cwd1:
    cwd2 = cwd2+c
    if c=="\\":cwd2=cwd2+"\\"

lista = os.listdir(cwd2)

print(lista)


    
