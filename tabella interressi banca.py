while True:
    value = float(input("importo "))
    years = int(input("quanti anni? "))
    interests = int(input("tasso d'interessi"))
    count = 0
    cres = value

    print("    anno      saldo  ")
    print("   ","-"*15)
    
    while count < years:
        cres = cres + (0.05*cres)
        count = count + 1
        print("%6.d %12.2f" % (count, cres))
    
    
