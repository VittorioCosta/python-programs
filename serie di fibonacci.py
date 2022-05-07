n = int(input("SERI DI FIBONACCI ---> "))
m = 0
val_p = 1
val_pp = 1
lista =[]
              
while m < n:
    lista.append(m)
    m += 1
    


while n < 2:
    if n == 0: print(1)
    if n == 1:print(1)

print(val_pp)


m = 1
while m < n:
    val = val_p + val_pp
    print(val)
    val_pp = val_p
    val_p = val
    m +=1
