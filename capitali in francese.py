nome_input = str(input("INPUT "))
nome = nome_input.capitalize()

except_ = ("Belize Camboge Mexique Monzabique Zaire Zimbabwe")
vocals_ = ("A E I O U")
u = nome[-1:0]

vocale=0
f=0

if nome[0] in vocals_ and ("-" not in nome):  print("l'" + nome)
elif nome in except_:  print("le " + nome)
elif u == "e":  print("la " + nome)
elif u!="e":
    if "-" in nome: print("les " + nome)
    else: print("le " + nome)


    
