from tkinter import *

f = Tk()
f.geometry("350x230")
f.title = ("ciao")
f.configure(bg = 'white')

canv = Canvas(f,width=350, height=230)
canv.pack()

mycolor = '#FFC0CB'
mycolor2 = '#%02x%02x%02x' % (255, 255, 0)  
mycolor3 = '#%02x%02x%02x' % (255,0, 0)

canv.create_oval(10,10,140,140,width=6, outline="blue")
canv.create_oval(110,10,240,140,width=6, outline=mycolor2)
canv.create_oval(210,10,340,140,width=6, outline="black")
canv.create_oval(60,90,190,220,width=6, outline="green")
canv.create_oval(160,90,290,220,width=6, outline=mycolor3)
