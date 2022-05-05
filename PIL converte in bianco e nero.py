from PIL import Image
img1 = Image.open("napoli.jpg")
img1.convert(mode="L").save("im2_b&n.jpg")

