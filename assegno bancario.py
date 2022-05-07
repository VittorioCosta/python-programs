from tkinter import *

finestra = Tk()
mycolor1 = '#%02x%02x%02x' % (223, 223, 223)  

finestra.title("assegno")
finestra.geometry("500x220")

canvas = Canvas(finestra, width=500, height=220)
canvas.pack()

canvas.create_rectangle(10,10,490,210, width=2, fill = mycolor1)
canvas.create_text(50,32,text="BANCA SELENIA",width=80,font=("Courier",14))
canvas.create_line(93,13,93,50, width = 1 )
canvas.create_text(140,31, text ='''123 gorgie road
EH11 2NS
Edinburgh''')
canvas.create_text(300,31,text="Publisher Bank of Scotland\n2000 price blvd\nEdinburgh, Scotland",font=("Courier",7))
canvas.create_text(450,28,text="CECK\nNUMBER")
canvas.create_text(450,55,text="063331")
canvas.create_text(250, 195, text="E478108240E      2006 20375  1301",font=("Calibri",14))
canvas.create_line(40,140,195,140, width = 1 )
canvas.create_line(20,180,480,180, width = 1 )


## Start programma
wh=8.65
eh=wh+wh*0.5
nw=40*wh
 



def main():
    nome = str(input("nome---> "))
    ore = float(input("ore---> "))
    w=nw + extra(ore)
    w=round(w,2)
    stampa(nome,w)
    return
    



def extra(ore):
    if ore > 40: extra = ore - 40
    elif ore <= 40: extra = 0
    return extra * eh
    
def stampa(nome,w):
    w_string = str(w)
    w_cent = w_string[-2:]
    w_int= int(w)
    w_intname = intName(w_int)
    canvas.create_text(115,75,text=nome, font=("georgia",16))
    canvas.create_text(115,95,text="08/08/2020", font=("Courier",10))
    canvas.create_text(350,85,text = "***" + w_string + "***", font=("georgia",16))
    canvas.create_text(350,110,text = "***" + w_intname + " " +
                       w_cent + "/100"+ "***",font=("georgia",10))
    canvas.mainloop()






def intName(number) :
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number. 

   if part >= 100 :
      name = digitName(part // 100) + " hundred"
      part = part % 100

   if part >= 20 :
      name = name + " " + tensName(part)
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0

   if part > 0 :
      name = name + " " + digitName(part)

   return name

## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(digit) :
   if digit == 1 : return "one"
   if digit == 2 : return "two"
   if digit == 3 : return "three"
   if digit == 4 : return "four"
   if digit == 5 : return "five"
   if digit == 6 : return "six"
   if digit == 7 : return "seven"
   if digit == 8 : return "eight"
   if digit == 9 : return "nine"
   return ""

## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#
def teenName(number) :
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "fifteen"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   return ""

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#
def tensName(number) :
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""

main()

    
    
    
    



    


