


run = [1,2,8,8,5,4,8,99,99,5,5,4,6,3,5,2,2,2,2,2,4,8,55,97]

def main():
    count = 1
    massimo = 1
    for i in range(1,len(run)):
        if run[i] == run[i-1]:
            count +=1
            if count > massimo:
                massimo=count
        if run[i] != run[i-1]: count = 1
    return print(massimo)
main()
        



        

