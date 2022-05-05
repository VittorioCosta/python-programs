from tkinter import *

f = Tk()
f.geometry("500x300")
f.title = ("ciao")

canv = Canvas(f,width=500, height=300)
canv.pack()


mycolor2 = '#FFC0CB'
canv.create_rectangle(100,100,200,200, fill=mycolor2)

mycolor2 = '#%02x%02x%02x' % (128, 0, 128)  
canv.create_rectangle(300,100,400,200, fill=mycolor2)
