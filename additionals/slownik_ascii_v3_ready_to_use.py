# chr, ord
def inputowanie():
    tekst = input('Wpisz:  ')

    return tekst


inp = inputowanie()


def wyswietleniezasz():
    lista = []
    for elem in inp:
        elem2 = ord(elem)
        lista.append(elem2)
    # print(lista)
    return lista


def szyfrowanie():
    lista = []
    for elem in inp:
        elem2 = ord(elem) - 3  # MINUS 3
        lista.append(elem2)
    # print(lista)
    return lista


def przechow(arg):
    print(f'przechow funk  {arg}')
    return (list(arg))


asci = przechow(szyfrowanie())


def nalitery():
    lista3 = []
    for elem in asci:
        elem2 = chr(elem)
        lista3.append(elem2)

    return lista3


print('\nz liter, ASCI base')
przechow(szyfrowanie())

print('\nz liter ASCI base -3')
przechow(wyswietleniezasz())

print('\nna litery ASCI po zmianie -3')
przechow(nalitery())
