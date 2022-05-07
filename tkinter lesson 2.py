from tkinter import*

def controlla():
    print(valore.get())

f = Tk()

valore = StringVar()

f.title("Finestra")
f.geometry("400x500")
f.configure(bg = "#589cf1")

casella = Checkbutton(f, text="conosci python", onvalue="SI", offvalue="NO", variable=valore, command=controlla)
casella.pack(pady=5)
casella.deselect()

f.mainloop()
