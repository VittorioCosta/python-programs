from tkinter import*

f = Tk()

tela = Canvas(f, width=300, height=300)
tela.pack()


f.title("Bandiera Italiana")
f.geometry("300x300")
f.configure(bg = "#589cf1")




tela.create_rectangle(100, 100, 130, 160, fill="green", outline="green")
tela.create_rectangle(130,100,160,160,fill="white", outline="white")
tela.create_rectangle(160,100,190,160,fill="red",outline="red")
tela.create_line(130,100,160,100)
tela.create_line(130,160,160,160)
