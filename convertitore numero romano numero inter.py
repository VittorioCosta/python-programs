




def main():
    romano=(input("---> "))
    print(numero(romano))
    return


def numero(romano):
    totale = 0
    while romano != "": 
        if len(romano) != 1:
            if numInt(romano[0]) >= numInt(romano[1]):
                totale = totale + numInt(romano[0])
                romano = romano[1:]
            elif numInt(romano[0]) < numInt(romano[1]):
                totale = totale - numInt(romano[0])
                romano = romano[1:]
        elif len(romano) == 1: 
            totale = totale + numInt(romano[0])
            romano = ""
    return totale

def numInt (r):
    if r == "M": n = 1000
    elif r == "D": n = 500
    elif r == "C": n = 100
    elif r == "L": n = 50
    elif r == "X": n = 10
    elif r == "V": n = 5
    elif r == "I": n = 1
    return n

main()