from tkinter import*

def test():
    messaggio = testo.get(0.0, END)
    print(messaggio)


f = Tk()

testo = Text(f, font="courier", insertwidth=10)
testo.pack()

b = Button(f, text="PREMI", command=test)
b.pack()

f.mainloop()
