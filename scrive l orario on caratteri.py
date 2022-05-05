##ritorna l'orario scritto in caratteri.
# param ora e minuti
# return orario scritto in lettere
#

def main():    
    hours = int(input("inserire ora---> "))
    minutes = int(input("inserire minuti---> "))
    ("\n")
    print(getTimeName(hours, minutes))
    return

def getTimeName(h, m):
    name = ""
    if m == 0: # caso o'clock
        if h <= 9: name = digitName(h) + " " + "o'clock"
        else: name = teenName(h) + " " + "o'clock"
    elif m < 40: #past
        if m == 15: name = "quarter past" + " " +  digitName(h)
        elif m == 30: name = "half past" + " " +  digitName(h)
        elif m < 9: name = digitName(m) + " past " + digitName(h) 
        elif m < 20: name = teenName(m) + "past" + digitName(h) 
        elif m < 40:
            parte = m % 10
            intero = m//10
            if m%10 != 0: name = tensNumber(intero) + " " + digitNumber(parte) + "past" + digitName(h)
            else: name = tensNumber(m) + " past " + digitNumber(h)
    elif m >= 40 and h != 12:
        if m==40: name = "twenty to " + digitName(h+1)
        elif m==50: name = "ten to " + digitName(h+1)
        elif m==45: name = "quarter to " + digitName(h+1)
        elif m==55: name = "five to " + digitName(h+1)
        else:
            diff = 60 - m
            if diff < 10: name = digitName(diff) + " to " + digirName(h+1)
            elif diff > 10:
                name = teenName(diff) + " to " + digitName(h+1)
    elif m >= 40 and h == 12:
        if m==40: name = "twenty to " + digitName(1)
        elif m==50: name = "ten to " + digitName(1)
        elif m==45: name = "quarter to " + digitName(1)
        elif m==55: name = "five to " + digitName(1)
        else:
            diff = 60 - m
            if diff < 10: name = digitName(diff) + " to " + digirName(1)
            elif diff > 10:
                name = teenName(diff) + " to " + digitName(1)
            
        
         
        
    
    return name

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
   if digit == 10 : return "ten"
   if digit == 11 : return "eleven"
   if digit == 12 : return "twelve"
   return 

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
   return

def tensName(number) :   
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return 
