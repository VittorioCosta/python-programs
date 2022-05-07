from tkinter import*
from tkinter import messagebox

def test():
    value = messagebox.askyesno("Domanda","vuoi inviare una mail")
    print(value)
    
f = Tk()


t = Button(f, text="premi qui", command=test)
t.grid()

f.mainloop()
