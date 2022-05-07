import os

newroot = "C:\\Users\\slelenia\\Desktop"
oldroot = "C:\\Users\\slelenia\\AppData\\Local\\Programs\\Python\\Python38"

os.chdir(newroot)
lista = os.listdir()




for name in lista:
    if name.endswith(".txt"): print(name)

os.chdir(oldroot)

exit
