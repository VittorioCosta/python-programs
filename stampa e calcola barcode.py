##costanti della tabella delle cifre

Cifra1 = ":::||"
Cifra2 = "::|:|"
Cifra3 = "::||:"
Cifra4 = ":|::|"
Cifra5 = ":|:|:"
Cifra6 = ":||::"
Cifra7 = "|:::|"
Cifra8 = "|::|:"
Cifra9 = "|:|::"
Cifra0 = "||:::"

Climit = "|"

##scelta se si vuole convertire un postcode oppure un barcode
# param postcode o barcode
# return barcode o postcode
def main():
    scelta = str(input("DO YOU WANT BARCODE(B) OR POSTCODE(P)??---> "))
    scelta = scelta.upper()
    print(printDigit(scelta))
    return

##ritorna un barcode o postcode in base alla scelta
# param B o P
# return barcode o postcode
def printDigit(scelta):
    if scelta == "B":
        postcode = int(input("INPUT POSTCODE---> "))
        while postcode < 10000 or postcode > 99999:   #postcode ceck
            postcode = int(input("INPUT A VALID POSTCODE!!!---> "))
        a = printBarcode(postcode)
    elif scelta == "P":
        lista = ("|",":")
        barcode = str(input("INPUT A BARCODE---> "))
        #barcode ceck
        if len(barcode)!= 32:barcode = str(input("INPUT A VALID BARCODE---> "))
        for n in range(0,len(barcode)):
            if barcode[n] not in lista:barcode = str(input("INPUT A VALID BARCODE---> "))
        a = readBarcode(barcode)
    a = str(a)
    return a

##dato un postcode restituisce un barcode con la cifra di controllo
# param int postcode
# return str barcode completo
def printBarcode(postcode):
    b = digitControl(postcode)
    postcode1=str(postcode)
    a = ""
    for n in range(0, len(postcode1)):
        if postcode1[n]=="1":a=a+Cifra1
        elif postcode1[n]=="2":a=a+Cifra2
        elif postcode1[n]=="3":a=a+Cifra3
        elif postcode1[n]=="4":a=a+Cifra4
        elif postcode1[n]=="5":a=a+Cifra5
        elif postcode1[n]=="6":a=a+Cifra6
        elif postcode1[n]=="7":a=a+Cifra7
        elif postcode1[n]=="8":a=a+Cifra8
        elif postcode1[n]=="9":a=a+Cifra9
        elif postcode1[n]=="0":a=a+Cifra0
    barcode = Climit + a + b + Climit
    return barcode

##dato un postcode restituisce la cifra di controllo
# param int postcode
# return str cifra di controllo
def digitControl(postcode):
    postcode = str(postcode)
    a = []
    c = 0
    lista = (0,1,2,3,4,5,6,7,8,9)
    for n in range(0, len(postcode)):
        b = postcode[n]
        b = int(b)
        a.append(b)
    for n in range(0,len(a)):
        c = c + a[n]
    for n in range(0,len(lista)):
        if (c + lista[n])%10 == 0: d = lista[n]
    if d == 1: d = Cifra1
    elif d == 2: d = Cifra2
    elif d == 3: d = Cifra3
    elif d == 4: d = Cifra4
    elif d == 5: d = Cifra5
    elif d == 6: d = Cifra6
    elif d == 7: d = Cifra7
    elif d == 8: d = Cifra8
    elif d == 9: d = Cifra9
    elif d == 0: d = Cifra0
    return d

def readBarcode(barcode):
    part1 = barcode[1:6]
    part2 = barcode[6:11]
    part3 = barcode[11:16]
    part4 = barcode[16:21]
    part5 = barcode[21:26]
    
    if part1 == Cifra1 : a = "1"     
    elif part1 == Cifra2 : a = "2"
    elif part1 == Cifra3 : a = "3"
    elif part1 == Cifra4 : a = "4"
    elif part1 == Cifra5 : a = "5"
    elif part1 == Cifra6 : a = "6"
    elif part1 == Cifra7 : a = "7"
    elif part1 == Cifra8 : a = "8"
    elif part1 == Cifra9 : a = "9"
    elif part1 == Cifra0 : a = "0"

    if part2 == Cifra1 : b = "1"     
    elif part2 == Cifra2 : b = "2"
    elif part2 == Cifra3 : b = "3"
    elif part2 == Cifra4 : b = "4"
    elif part2 == Cifra5 : b = "5"
    elif part2 == Cifra6 : b = "6"
    elif part2 == Cifra7 : b = "7"
    elif part2 == Cifra8 : b = "8"
    elif part2 == Cifra9 : b = "9"
    elif part2 == Cifra0 : b = "0"    
    
    if part3 == Cifra1 : c = "1"     
    elif part3 == Cifra2 : c = "2"
    elif part3 == Cifra3 : c = "3"
    elif part3 == Cifra4 : c = "4"
    elif part3 == Cifra5 : c = "5"
    elif part3 == Cifra6 : c = "6"
    elif part3 == Cifra7 : c = "7"
    elif part3 == Cifra8 : c = "8"
    elif part3 == Cifra9 : c = "9"
    elif part3 == Cifra0 : c = "0" 
        
    if part4 == Cifra1 : d = "1"     
    elif part4 == Cifra2 : d = "2"
    elif part4 == Cifra3 : d = "3"
    elif part4 == Cifra4 : d = "4"
    elif part4 == Cifra5 : d = "5"
    elif part4 == Cifra6 : d = "6"
    elif part4 == Cifra7 : d = "7"
    elif part4 == Cifra8 : d = "8"
    elif part4 == Cifra9 : d = "9"
    elif part4 == Cifra0 : d = "0" 

    if part5 == Cifra1 : e = "1"     
    elif part5 == Cifra2 : e = "2"
    elif part5 == Cifra3 : e = "3"
    elif part5 == Cifra4 : e = "4"
    elif part5 == Cifra5 : e = "5"
    elif part5 == Cifra6 : e = "6"
    elif part5 == Cifra7 : e = "7"
    elif part5 == Cifra8 : e = "8"
    elif part5 == Cifra9 : e = "9"
    elif part5 == Cifra0 : e = "0"

    code = a+b+c+d+e
    return code

main()
    
    




        
        
            
        
        
        
    
    
















   
