from sys import argv


file2 = argv[1]
a = open(file2,"r")

lista=[]

for line in a:
    line = line.rstrip("\n")
    new=""
    for i in range(len(line)-1,-1,-1):
        
        new=new+line[i]
    lista.append(new)
    
a.close()


a = open(file2,"w")

for line in lista:
    line += "\n"
    a.write(line)
    
a.close()

