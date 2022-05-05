from tkinter import *

r=0
g=0
b=255
color = 65536*r+256*g+b
color = str(color)

def main():
    temp= float(input("TEMPERATURE 0°-100°--->"))
    while temp<0 or temp>100:
        temp= float(input("TEMPERATURE 0°-100°--->"))   
    colorForValue(temp)
    f = Tk()
    f.geometry("500x300")
    f.title = ("ciao")
    canv = Canvas(f,width=500, height=300)
    canv.pack()
    mycolor2 = '#%02x%02x%02x' % (r, g, b)  
    canv.create_rectangle(125,25,375,100, fill=mycolor2)
    canv.create_text(250,200, text=color,font=("Courier",20))    
    return

def colorForValue(t):
    global r
    global g
    global b
    if t>=0 and t<25:
        r = 0
        b = 255
        z = (t-0)/(25-0)
        g = int(0*(1-z)+255*z)
    elif t>=25 and t<=50:
        r = 0
        g = 255
        z = (t-25)/(50-25)
        b = int(255*(1-z)+0*z)
    elif t>50 and t<=75:
        g = 255
        b = 0
        z = (t-50)/(75-50)
        r = int(0*(1-z)+255*z)
    elif t>75 and t<=100:
        r = 255
        b = 0
        z = (t-75)/(100-75)
        g = int(255*(1-z)+0*z)        
    return        
        
main()