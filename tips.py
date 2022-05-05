a = int(input('''satisfaction level:
1. full satisfaction
2. satisfaction
3. unsatisfaction
'''))
c = float(input("bill "))

f = c*0.2
s = c*0.1

if a == 1: print("the tips is %.0f" % f)
elif a == 2: print("the tips is %.0f" % s)
if a == 3: print("you can pay your bill, the tips isn't considerate")
