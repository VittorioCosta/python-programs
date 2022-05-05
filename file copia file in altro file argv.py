## copia il testo riga per riga di un file in un altro file
## una argv
from sys import argv
import os
def main():
    try:                    # imposto un blocco try nel caso non ci fossero agrv
        fileIn=argv[1]
        fileOut=argv[2]
        fileIn = open(fileIn,"r")
        fileOut = open(fileOut,"w")

        for line in fileIn:
            fileOut.write(line)

        fileIn.close()
        fileOut.close()
    
    except IndexError:
        fileIn = input("input file---> ")
        while not os.path.isfile(fileIn):
            a = os.listdir()
            print("the files in cwd are:",a)
            print("invalid file name")
            fileIn = input("input file---> ")

        fileOut = input("Output file---> ")
        while not os.path.isfile(fileOut):
            a = os.listdir()
            print("the files in cwd are:",a)
            print("invalid file name")
            filename = input("output file---> ")

        fileIn = open(fileIn,"r")
        fileOut = open(fileOut,"w")

        for line in fileIn:
            fileOut.write(line)

        fileIn.close()
        fileOut.close()
    
main()
        

    
