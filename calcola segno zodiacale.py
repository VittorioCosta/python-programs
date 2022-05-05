a = int(input("day "))
b = int(input("month "))

if(b == 1 and a >= 21) or(b==2 and a<=19):
    print("Aquario")
elif(b == 2 and a >= 20) or(b==3 and a<=20):
    print("pesci")
elif(b ==21  and a >=21 ) or(b==4 and a<=20):
    print("ariete")
elif(b ==4  and a >=21 ) or(b==5 and a<=21):
    print("TORO")
elif(b == 5 and a >=22 ) or(b==6 and a<=21):
    print("Gemelli")
elif(b == 6 and a >= 22) or(b==7 and a<=23):
    print("cancro")
elif(b == 7 and a >= 23) or(b==8 and a<=23):
    print("leone")
elif(b == 8 and a >=24 ) or(b==9 and a<=23):
    print("vergine")
elif(b ==10  and a >=24 ) or(b==11 and a<=22):
    print("scorpione")
elif(b ==11   and a >=23 ) or(b==12 and a<=21):
    print("saggittario")
elif(b ==12  and a >=22 ) or(b==1 and a<=20):
    print("capricorno")


