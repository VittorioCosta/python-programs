a = float(input("insert a float number "))
b = float(input("insert a float number "))

a = round(a, 2)
b = round(b, 2)
c = abs(a - b)
c=round(c, 2)


if c <= 0.01: print("i numeri sono uguali ")
else: print("i numeri sono diversi")


