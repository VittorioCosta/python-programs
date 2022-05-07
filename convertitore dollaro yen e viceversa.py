print("convertitore in yen")

one_dollar = float(input("valore di un dollaro in yen "))
a = 1


while a != 0:
    a = float(input("dollari---> "))
    if a != 0:
        a = a*one_dollar
        print(a)
    
    
a = 1
print("convertitore in dollari")

while a!=0:
    a = float(input("yen---> "))
    if a != 0:
        a = a/one_dollar
        print(a)
