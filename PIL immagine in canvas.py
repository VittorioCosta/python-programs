from tkinter import *

# pip install pillow
from PIL import Image
from PIL import ImageTk

root = Tk()

root.geometry("600x600")

canvas = Canvas(root,width=800,height=800)
canvas.pack()


load = Image.open("OIP.JPG")
render = ImageTk.PhotoImage(load)


canvas.create_image(400,400,image=render)
