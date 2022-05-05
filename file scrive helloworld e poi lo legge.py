file = open("C:\\Users\\slelenia\\Desktop\\vitWork\\hello.txt","w")
file.write("hello world!")
file.close()

file = open("C:\\Users\\slelenia\\Desktop\\vitWork\\hello.txt","r")
line = file.readline()
print(line)
file.close()
