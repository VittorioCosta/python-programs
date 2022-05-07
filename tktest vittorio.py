from tkinter import *

f = Tk()
f.geometry("300x300")
f.title = ("ciao")

canv = Canvas(f,width=300, height=300)
canv.pack()
canv.create_rectangle(75,100,225,200, fill = "blue")
canv.create_text(150,150, text="Vittorio",width=130, font=("courier",20))

