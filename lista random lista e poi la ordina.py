import random

def main():
    lista = []
    for i in range(60):
        a = random.randint(1,99)
        lista.append(a)
    print(lista)
    print('''\nLISTA ORDINATA: \n''')
    lista.sort()
    print(lista)
main()
