a = 0
tot = 0

while a != 100:
    print("persone nel locale:%3.d"% tot)
    a = int(input("---> "))
    while a > (100-tot):
        a = int(input("max 100 persone ---> "))
    tot +=a

print("persone nel locale:%3.d"% tot)
exit
