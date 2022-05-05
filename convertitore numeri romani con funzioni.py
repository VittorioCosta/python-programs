stringa = ""

def main():
    b=int(input("numero---> "))
    while b > 3999:
        b=int(input("numero---> "))
    print("\n")
    print(romeNumbers(b))
    return

def romeNumbers(number):
    global stringa
    if number // 1000 > 0:
        stringa = stringa + tousand(number//1000)
        number = number % 1000
    if number // 100 > 0:
        stringa = stringa + cent(number//100)
        number = number % 100
    if number // 10 > 0:
        stringa = stringa + dec(number//10)
        number = number % 10
    if number <= 9: stringa = stringa + unit(number)
    return stringa
    
    
    

def unit(b):
    if b == 0: u=""
    elif b == 1: u="I"
    elif b == 2: u="II"
    elif b == 3: u="III"
    elif b == 4: u="IV"
    elif b == 5: u="V"
    elif b == 6: u="VI"
    elif b == 7: u="VII"
    elif b == 8: u="VIII"
    elif b == 9: u="IX"
    return u

def dec(b):
    if b == 1: d="X"
    elif b == 2: d="XX"
    elif b == 3: d="XXX"
    elif b == 4: d="XL"
    elif b == 5: d="L"
    elif b == 6: d="LI"
    elif b == 7: d="LII"
    elif b == 8: d="LIII"
    elif b == 9: d="XC"
    return d

def cent(b):
    if b == 1: c="C"
    elif b == 2: c="CC"
    elif b == 3: c="CCC"
    elif b == 4: c="CD"
    elif b == 5: c="D"
    elif b == 6: c="DC"
    elif b == 7: c="DCC"
    elif b == 8: c="DCCC"
    elif b == 9: c="CM"
    return c

def thousand(b):
    if b == 1: m="M"
    elif b == 2: m="MM"
    elif b == 3: m="MMM"
    return m
main()
    
    
    
