from tkinter import*

def cambia(evento):
    testo.configure(text=casella_testo.get())

def elimina():
    casella_testo.delete(0,END) 
    
f = Tk()

f.title("Finestra")
f.geometry("400x500")
f.configure(bg = "#589cf1")

testo = Label(f, text="SUD\nJaMm", font = "Times 22 bold")
testo.pack()
testo.configure(background="#589cf1")

casella_testo = Entry(f, show="*")
casella_testo.pack(pady="5")
casella_testo.focus_set()
casella_testo.insert(0, "scrivi qui")
casella_testo.configure(justify=CENTER)
casella_testo.bind("<Return>",cambia)

b = Button(f, text="premi qui", command = cambia)
b.pack()

b = Button(f, text="ELIMINA", command = elimina)
b.pack()

f.mainloop()
