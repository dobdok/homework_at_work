# chr, ord
def inputowanie():
    tekst = input('Wpisz:  ')

    return tekst


def przechow(arg):
    print(f'przechow funk  {arg}')


def szyfrowanie():
    lista = []
    for elem in inputowanie():
        elem2 = ord(elem)
        lista.append(elem2)
    print(lista)


szyfrowanie()
