while True:
    a = int(input('''do you want a description about:
    1. wave lenght (mt)
    2. frequency  (Hz)\n'''))

    b = float(input("value "))

    c = ("radio waves","microwaves","undered","light","ultraviolet","x ray","gamma ray")

    if a == 1:
        if b>10**-1: r = c[0]
        elif b<= 10**-1 and b>10**-3: r = c[1]
        elif b<= 10**-3 and b>7*10**-7: r = c[2]
        elif b<= 4*10**-7 and b>7*10**-7: r = c[3]
        elif b<= 7*10**-7 and b>10**-8: r = c[4]
        elif b<= 10**-8 and b>10**-11: r = c[5]
        elif b<=10**-11: r = c[6]
    elif a == 2:
        if b<3*10**9: c[0]
        elif b>=3*10**9 and b<3*10**11: r = c[1]
        elif b>=3*10**11 and b<4*10**14: r = c[2]
        elif b>=4*10**14 and b<7.5*10**14: r = c[3]
        elif b>=7.5*10**14 and b<3*10**16: r = c[4]
        elif b>=3*10**16 and b<3*10**19: r = c[5]
        elif b>=3*10**19: r = c[6]

    print("\n")

    print(" the electromagnetic spectrum: " + r +"\n\n")
