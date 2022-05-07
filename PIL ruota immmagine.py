from PIL import Image
img1 = Image.open("OIP.jpg")
img1.rotate(90).save("OIP_rotata.jpg")

