cc = float(input("CC "))
ccr = float(input("CCR "))

if cc<0 or ccr<0: print("il conto é in negativo"), exit
print("\n")

o = int(input('''operazione:
1. Deposito
2. Prelievo
3. Bonifico\n'''))

s = float(input("somma da operare "))

if s<0: print("il valore è negativo"), exit
elif o==1: cc+=s
elif o==2: cc-=s
elif o==3: ccr+=s

if o==3: cc-=s
print("\nSaldo CC:%5.2f\nSaldo CCR:%4.2f" % (cc, ccr))


