from random import randint

def scramble(word):
    lista = []
    d = randint(1, len(word)-2)
    e = randint(1, len(word)-2)
    while d == e:
        e = randint(1, len(word)-2)
    lista.append(d)
    lista.append(e)
    a = min(lista)
    b = max(lista)
    x = word[a]
    y = word[b]
    z = word[:a] + y + word[a+1:b] + x + word[b+1:]
    return z
