while True:
    print("ciao, ti mostro quanto manca all'ora X\n")
    time = str(input("inserci l'ora corrente in formato militare ---> "))
    print("\n")
    time_two = str(input("inserisci l'ora X ---> "))
    print("\n\n")

    minut = time[2:4]
    hour = time[0:2]
    minut_two = time_two[2:4]
    hour_two = time_two[0:2]

    minut_int = int(minut)
    hour_int = int(hour)

    minut_two_int = int(minut_two)
    hour_two_int = int(hour_two)

    hour_out_one = (hour_two_int - hour_int)
    hour_out_two = (24 - hour_int + hour_two_int)
    hour_out_one_less = (hour_out_one - 1)
    hour_out_two_less = (hour_out_two - 1)
    minut_out_one = (minut_two_int - minut_int)
    minut_out_two = (60 - minut_int + minut_two_int)
    minut_out_three = (60 - minut_int + minut_two_int)
    

    if hour_int <= hour_two_int and minut_int <= minut_two_int:
        print("mancano %.d ore e %.d minuti all'ora X" % (hour_out_one, minut_out_one))
    elif hour_int < hour_two_int and minut_int >= minut_two_int:
        print("mancano %.d ore e %.d minuti all'ora X" % (hour_out_one_less, minut_out_two))
    elif hour_int > hour_two_int and minut_int >= minut_two_int:
        print("mancano %.d ore e %.d minuti all'ora X" % (hour_out_two_less, minut_out_two))
    elif hour_int >= hour_two_int and minut_int <= minut_two_int:
        print("mancano %.d ore e %.d minuti all'ora X" % (hour_out_two, minut_out_one))
    elif hour_int == hour_two_int and minut_int >= minut_two_int:
        print("mancano 23 ore e %.d minuti all'ora X" % (minut_out_three))
    
    


      

