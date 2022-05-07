while True:
    a = int(input("number "))
    b = str(a)

    if a > 3999:
        print("the number is to big"), exit()

    if len(b) == 1:
        if b == "0": u="nullo"
        elif b == "1": u="I"
        elif b == "2": u="II"
        elif b == "3": u="III"
        elif b == "4": u="IV"
        elif b == "5": u="V"
        elif b == "6": u="VI"
        elif b == "7": u="VII"
        elif b == "8": u="VIII"
        elif b == "9": u="IX"

    if len(b) == 2:
        if b[0] == "1": d="X"
        elif b[0] == "2": d="XX"
        elif b[0] == "3": d="XXX"
        elif b[0] == "4": d="XL"
        elif b[0] == "5": d="L"
        elif b[0] == "6": d="LI"
        elif b[0] == "7": d="LII"
        elif b[0] == "8": d="LIII"
        elif b[0] == "9": d="XC"

    if len(b) == 2:
        if b[1] == "0": u=""
        elif b[1] == "1": u="I"
        elif b[1] == "2": u="II"
        elif b[1] == "3": u="III"
        elif b[1] == "4": u="IV"
        elif b[1] == "5": u="V"
        elif b[1] == "6": u="VI"
        elif b[1] == "7": u="VII"
        elif b[1] == "8": u="VIII"
        elif b[1] == "9": u="IX"

    if len(b) == 3:
        if b[0] == "1": c="C"
        elif b[0] == "2": c="CC"
        elif b[0] == "3": c="CCC"
        elif b[0] == "4": c="CD"
        elif b[0] == "5": c="D"
        elif b[0] == "6": c="DC"
        elif b[0] == "7": c="DCC"
        elif b[0] == "8": c="DCCC"
        elif b[0] == "9": c="CM"

    if len(b) == 3:
        if b[1] == "0": d=""
        elif b[1] == "1": d= "X"
        elif b[1] == "2": d="XX"
        elif b[1] == "3": d="XXX"
        elif b[1] == "4": d="XL"
        elif b[1] == "5": d="L"
        elif b[1] == "6": d="LX"
        elif b[1] == "7": d="LXX"
        elif b[1] == "8": d="LXXX"
        elif b[1] == "9": d="XC"

    if len(b) == 3:
        if b[2] == "0": u=""
        elif b[2] == "1": u="I"
        elif b[2] == "2": u="II"
        elif b[2] == "3": u="III"
        elif b[2] == "4": u="IV"
        elif b[2] == "5": u="V"
        elif b[2] == "6": u="VI"
        elif b[2] == "7": u="VII"
        elif b[2] == "8": u="VIII"
        elif b[2] == "9": u="IX"
        

    if len(b) == 4:
        if b[0] == "1": m="M"
        elif b[0] == "2": m="MM"
        elif b[0] == "3": m="MMM"

    if len(b) == 4:
        if b[1] == "0": c=""
        elif b[1] == "1": c="C"
        elif b[1] == "2": c="CC"
        elif b[1] == "3": c="CCC"
        elif b[1] == "4": c="CD"
        elif b[1] == "5": c="D"
        elif b[1] == "6": c="DC"
        elif b[1] == "7": c="DCC"
        elif b[1] == "8": c="DCCC"
        elif b[1] == "9": c="CM"

    if len(b) == 4:
        if b[2] == "0": d="X"
        elif b[2] == "1": d="X"
        elif b[2] == "2": d="XX"
        elif b[2] == "3": d="XXX"
        elif b[2] == "4": d="XL"
        elif b[2] == "5": d="L"
        elif b[2] == "6": d="LX"
        elif b[2] == "7": d="LXX"
        elif b[2] == "8": d="LXXX"
        elif b[2] == "9": d="XC"

    if len(b) == 4:
        if b[3] == "0": u=""
        elif b[3] == "1": u="I"
        elif b[3] == "2": u="II"
        elif b[3] == "3": u="III"
        elif b[3] == "4": u="IV"
        elif b[3] == "5": u="V"
        elif b[3] == "6": u="VI"
        elif b[3] == "7": u="VII"
        elif b[3] == "8": u="VIII"
        elif b[3] == "9": u="IX"

    if len(b) == 1: print(u)
    elif len(b) == 2: print(d + u)
    elif len(b) == 3: print(c + d + u)
    elif len(b) == 4: print(m + c + d + u)

    print("\n")
