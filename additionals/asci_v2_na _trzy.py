# chr, ord

def pokaz_zakodowane():
    li = inputowanie()  # tuple / list
    # print(type(inputowanie()))
    lista = []
    for elem in li[0]:
        elem2 = int(ord(elem)) + int(li[1])
        lista.append(elem2)

    lista2 = []
    ret = ''
    for i in lista:
        i = chr(i)
        lista2.append(i)
        ret = ''.join(str(t) for t in lista2)

    print('zakodowanie: ', ret)


def pokaz_rozkodowane():
    li = inputowanie()  # tuple / list
    # print(type(inputowanie()))
    lista = []
    for elem in li[0]:
        elem2 = int(ord(elem)) - int(li[1])
        lista.append(elem2)

    lista2 = []
    ret = ''
    for elem5 in lista:
        elem5 = chr(elem5)
        lista2.append(elem5)
        ret = ''.join(str(elem7) for elem7 in lista2)

    print('rozkodowanie:', ret)


def inputowanie():   # wersja1
    list_inp = []
    tekst1 = input('Wpisz tekst:  ') or ''
    tekst2 = input('Klucz szyfrowania:  ') or 3
    list_inp = [tekst1, tekst2]
    return list_inp   # list

# def inputowanie():   # wersja2
#     tekst1 = input('Wpisz tekst:  ') or ''
#     tekst2 = input('Klucz szyfrowania:  ') or 3
#     return tekst1, tekst2  # tuple


def glowne_pyt():
    finput = input(
        """ --  DECODING / ENCODING  --
        For decode/rozkoduj press 'd' or 'D'.
        for encode/zakoduj press 'e' or 'E'.
        My choice:  """
        )

    try:
        if finput.lower() == 'd':  # or finput == 'D':
            pokaz_rozkodowane()
            pokaz_zakodowane()  # to verify/test in pairs

        elif finput.lower() == 'e':
            pokaz_zakodowane()
            pokaz_rozkodowane()  # to verify/test in pairs

        else:
            print('wrong input')
            glowne_pyt()

    except ValueError:
        print('Not a good value')
        glowne_pyt()


glowne_pyt()
