from tkinter import*



f = Tk()




f.title("Finestra")
f.geometry("350x230")
f.configure(bg = "#589cf1")

tela = Canvas(f, width=350, height=230)
tela.pack()

tela.create_line(0, 0, 10, 70, fill="red", width=5)
tela.create_line(10, 70, 95, 30, dash=2)

tela.create_rectangle(20, 20, 80, 80, fill="blue", outline="red")

tela.create_oval(180,120,260,260, fill="blue", outline="red")
tela.create_polygon(10,10,140,40,120,150,70,180)
tela.create_text(110,230,text="CIAO A TUTTI",width=50,font=("Courier",10))


f.mainloop()
