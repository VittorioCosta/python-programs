from tkinter import*

def scrivi(evento):
    x = lista.curselection()[0]
    print(lista.get(x))

f = Tk()

f.title("Finestra")
f.geometry("400x500")
f.configure(bg = "#589cf1")

lista = Listbox(f)
lista.pack()
lista.insert(END,"uno","due","tre")
lista.insert(0, "inizio")
lista.delete(3,4)
lista.bind("<ButtonRelease-1>", scrivi)

f.mainloop()
