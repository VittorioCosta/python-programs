
a = "entrambe le porte sono chiuse"
s = "la porta sinistra si apre"
d = "la porta destra si apre"

var = [0 ,1 ,1 ,1 ,0 ,0 ,0 ,1 ,"P" ]



if var[8] != "P": print(a)
elif var[8] =="P": 
    if var[3] != 1: print(a)
    elif var[3] == 1:
        if var[2] != 1: print(a)
        elif var[2] == 1: ok = 1

if var[0] == 1 and ok ==1:
    if  var[4] or  var[6] ==1: print(s)

if var[1] == 1 and ok==1:
    if  var[5] or  var[7] ==1: print(d)

if (var[0] or var[1])==0 and ok==1: print(a)
elif(var[0] or var[1])==1 and (var[4] or var[5] or
                               var[6] or var[7])==0: print (a)







                
                
           
