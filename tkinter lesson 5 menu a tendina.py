from tkinter import*

def test(scelta):
    print("Ciao nella shell")

f = Tk()




f.title("Finestra")
f.geometry("400x500")
f.configure(bg = "#589cf1")

trasparente = Menu(f)
f.config(menu=trasparente)
primo_menu = Menu(trasparente)
trasparente.add_cascade(label="File", menu=primo_menu)
primo_menu.add_command(label="Apri...",command=test, accelerator="Alt-a")
primo_menu.add_command(label="ESCI",command=quit)



impostazioni = Menu(trasparente)
trasparente.add_cascade(label="Impostazioni ", menu=impostazioni)
impostazioni.add_command(label="cambia colore schermo",command=test)
impostazioni.add_command(label="cambia colore testo",command=test)
impostazioni.add_separator()
impostazioni.add_command(label="imposta variabili",command=test)

f.bind("<Alt-a>", test)


f.mainloop()
