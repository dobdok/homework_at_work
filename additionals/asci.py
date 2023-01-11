# chr, ord

def inputowanie():
    tekst = input('Wpisz:  ')

    return tekst


def inputowanie2():
    tekst = input('Klucz:  ') or 3

    return int(tekst)


inp = inputowanie()
inp2 = inputowanie2()


def szyfrowanie():
    lista = []
    for elem in inp:
        elem2 = ord(elem)
        lista.append(elem2)
    print(lista)
    return lista


def wyswietleniezasz():
    lista = []
    for elem in inp:
        elem2 = ord(elem) - inp2  # MINUS 3
        lista.append(elem2)

    return lista


def przechow(arg):

    return list(arg)


def nalitery():
    lista3 = []

    for elem in przechow(wyswietleniezasz()):
        elem2 = chr(elem)
        lista3.append(elem2)

    return lista3


# print('\nz liter, ASCI base')
# przechow(szyfrowanie())
#
# print('\nz liter ASCI base -3')
# przechow(wyswietleniezasz())

print('\ntekst po zaszyfrowaniu: ')


# przechow(nalitery())

def ustringowanie(arg):
    ret = ''.join(str(elem7) for elem7 in arg)
    print(ret)
    return ret


ustringowanie(przechow(nalitery()))

# 1. wiadsomosc, klucz    2. # odkod    3. # zakod
