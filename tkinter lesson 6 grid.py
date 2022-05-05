from tkinter import*

f = Tk()


f.title("Finestra")
f.geometry("400x500")
f.configure(bg = "#589cf1")

t = Button(f, text="tasto")
t.grid(column=0,row=0)

t1 = Button(f, text="tasto1")
t1.grid(column=1,row=0)



f.mainloop()
