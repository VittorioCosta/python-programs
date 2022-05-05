from PIL import Image, ImageFilter
img1 = Image.open("napoli.jpg")
img1.filter(ImageFilter.GaussianBlur(10)).save("im2_blur.jpg")
