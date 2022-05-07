from PIL import Image
dim = (200,200)
img1 = Image.open("napoli.jpg")
img1.thumbnail(dim)
img1.save("im2.png")
