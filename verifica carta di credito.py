num = "0000"


while len(num)!=8:
    num = str(input("number---> "))

a = (int(num[7]))
b = (int(num[6]))*2
c = (int(num[5]))
d = (int(num[4]))*2
e = (int(num[3]))
f = (int(num[2]))*2
g = (int(num[1]))
h = (int(num[0]))*2


    

dispari = a + c + e + g

b = str(b)
d = str(d)
f = str(f)
h = str(h)

y = 0
for n in range(len(b)):
    z = int(b[n])
    y += z

x = 0
for n in range(len(d)):
    z = int(d[n])
    x += z

w = 0
for n in range(len(f)):
    z = int(f[n])
    w += z

q = 0
for n in range(len(h)):
    z = int(h[n])
    q += z

pari = y + x + w + q

controllo = pari + dispari
controllo = str(controllo)

ultima = controllo[-1:]

if ultima == "0": print("il numero è corretto")
elif ultima != "0":
    for n in range(10):
        dispari1 = n+c+e+g
        controllo1 = dispari1 + pari
        controllo1 = str(controllo1)
        ultima1 = controllo1[-1:]
        if ultima1 == "0": print("valore jolly is %.d"% n)
            









