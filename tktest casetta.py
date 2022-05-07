from tkinter import *

f = Tk()
f.geometry("300x300")
f.title = ("ciao")

canv = Canvas(f,width=300, height=300)
canv.pack()

mycolor = '#FFC0CB'
mycolor2 = '#%02x%02x%02x' % (192, 192, 192)  
mycolor3 = '#%02x%02x%02x' % (140,237,244)

canv.create_rectangle(70,130,230,290, fill=mycolor,outline=mycolor)
canv.create_polygon(150,10,70,130,230,130,fill=mycolor2,outline=mycolor2)
canv.create_rectangle(102,170,134,290, fill="brown")
canv.create_rectangle(166,170,198,202, fill=mycolor3)

