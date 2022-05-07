from tkinter import *

f = Tk()
f.geometry("500x300")
f.title = ("ciao")

canv = Canvas(f,width=500, height=300)
canv.pack()




canv.create_oval(210,110,290,190,fill="black")
canv.create_oval(220,120,280,180,fill="white")
canv.create_oval(225,125,275,175,fill="black")
canv.create_oval(235,135,265,165,fill="white")
canv.create_oval(240,140,260,160,fill="black")
