l = int(input("side number ---> "))
a = " "
b = "*"
lista = []
count = 1


print((b*l)+" "+(b*l))

for n in range(1, l):
    c = (b*l)+a+b+(a*(l-2))+b
    print(c)

print((b*l)+" "+(b*l))
