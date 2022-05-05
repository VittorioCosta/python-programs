
from random import randint

a=str(input("vuoi lanciare la moneta?...s   n "))


while a!="n":
      if a=="s":
          b=randint(1,100)
          if b%2==0: print("testa")
          elif b%2==1: print("croce")
      a=str(input("vuoi lanciare la moneta?...s   n "))   
