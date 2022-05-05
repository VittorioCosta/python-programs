from random import *

g = str(input("modalità di gioco i/s "))
g.lower()
count = 0
print("\n")

while g != "s" and g != "i":
    g = str(input("modalità di gioco i/s "))
    g.lower()

m = randint(10, 100)
t = randint(0,1)
lista = [3,7,15,31,63]
lista1  = [7,15,31,63]
b = 0

if g == "s":
    if t == 0:
        print("a sto giro cominci tu...\n")
        while m != 1:
            print("ci sono %.d nel contenitore\n" % m)
            a = int(input("---> "))
            while a < 1 or  a > (m//2):
                a = int(input("---> "))
            m -= a
            count += 1
            if m != 1:
                print("ci sono %.d nel contenitore\n" % m)
                b = randint(1, m//2)
                print("il computer sceglie %.d" % b)
                m -= b
                count += 1
        if m == 1:
            if count%2==1:
                print("hai vinto")
                print('''   /\\
  /  \\
 /    \\
/      \\
--------
  "  "
  "  "
  "  "''')
            else: print("hai perso")
    if t == 1:
        print("a sto giro comincia il computer...\n")
        while m != 1:
            if m != 1:   #ciclo computer
                print("ci sono %.d nel contenitore\n" % m)
                b = randint(1, m//2)
                print("il computer sceglie %.d" % b)
                m -= b
                count += 1
            print("ci sono %.d nel contenitore\n" % m) # ciclo a
            a = int(input("---> "))
            while a < 1 or  a > (m//2):
                a = int(input("---> "))
            m -= a
            count += 1
        if m == 1:
            if count%2==1:
                print("hai vinto")
                print('''   /\\
  /  \\
 /    \\
/      \\
--------
  "  "
  "  "
  "  "''')
            else: print("hai perso")

elif g == "i":   #comp intel
    if t == 0:  #comincio io
        print("a sto giro cominci tu...\n")
        while m != 1:
            print("ci sono %.d nel contenitore\n" % m) #ciclo a
            a = int(input("---> "))
            while a < 1 or  a > (m//2):
                a = int(input("---> "))
            m -= a
            count += 1 #fine
            print("ci sono %.d nel contenitore\n" % m) #ciclo b
            if m in lista1:
                if m != 1:   
                    b = randint(1, m//2)
                    print("il computer sceglie %.d" % b)
                    m -= b
                    count += 1
            elif m not in lista1  and m!=2 and m!=3 and m!=4 and m !=5 and m != 6:
                b = 0
                while (m-b not in lista1) and m!=2 and m!=3 and m!=4 and m !=5 and m != 6 :
                    b = randint(1, m//2)
                print("il computer sceglie %.d" % b)
            
            elif m == 2:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 3:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 4:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 5:
                b = 2
                print("il computer sceglie %.d" % b)
            elif m == 6:
                b = 3
                print("il computer sceglie %.d" % b)
            
            m -= b   
            count +=1  #fine
        if m == 1:
            if count%2==1:
                print("hai vinto")
                print('''   /\\
  /  \\
 /    \\
/      \\
--------
  "  "
  "  "
  "  "''')
            elif count%2==0: print("hai perso")

                
    if t == 1:  #comincia computer
        print("a sto giro comincia il computer...\n")
        while m != 1:
            print("ci sono %.d nel contenitore\n" % m) #ciclo b
            if m in lista1:
                if m != 1:   
                    b = randint(1, m//2)
                    print("il computer sceglie %.d" % b)
                    m -= b
                    count += 1
            elif m not in lista1 and m!=2 and m!=3 and m!=4 and m !=5 and m != 6:
                b = 0
                while (m-b not in lista1)and m!=1 and m!=2 and m!=3 and m!=4 and m !=5 and m != 6 :
                    b = randint(1, m//2)
                print("il computer sceglie %.d" % b)
            
            elif m == 2:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 3:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 4:
                b = 1
                print("il computer sceglie %.d" % b)
            elif m == 5:
                b = 2
                print("il computer sceglie %.d" % b)
            elif m == 6:
                b = 3
                print("il computer sceglie %.d" % b)
                
            m -= b   
            count +=1  #fine
            while m !=1 and count != count + 1:
                print("ci sono %.d nel contenitore\n" % m) #ciclo a
                a = int(input("---> "))
                while a < 1 or  a > (m//2):
                    a = int(input("---> "))
                m -= a
                count += 1 #fine
    if m == 1:
        if count%2==1:
            print("hai perso")
            print('''   /\\
  /  \\
 /    \\
/      \\
--------
  "  "
  "  "
  "  "''')
        else: print("hai vinto")              
        
        
                
                

            
            
        
        
        

            
