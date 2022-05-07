a = int(input("numero"))

if a < 0: a=a*(-1)

if a < 10 and a<100 :  print("una cifra")
elif a >= 10 and a < 100: print ("2 cifre")
elif a >= 100 and a < 1000: print ("3 cifre")
elif a >= 1000 and a < 100000: print ("4 cifre")
elif a >= 10000 and a < 100000:print ("5 cifre")


    
