import os.path
def main():
    file=input("---> ")
    while not os.path.isfile(file):
        print("file don't exist")
        file=input("---> ")

    file = open(file,"r")
    for line in file:
        a = line.split()
        a[0]=float(a[0])
        a[1]=float(a[1])
        b = (a[0]+a[1])/2
        print(b)
    file.close()

main()
