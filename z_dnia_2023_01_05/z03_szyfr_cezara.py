"""Napisać program który będzie działał na zasadzie Szyfru Cezara

    Program powinien spytać użytkownika o czynność którą chce wykonać - kodowanie / odkodowanie
    Spytać o wiadomość
    Spytać o punkt przesunięcia, jeżeli uzytkownik nic nie poda to przyjmie domyślną wartość - 3
    Wyświetlić zakodowany / odkodowany tekst


"""

# chr, ord

def rozko_zako():

    try:
        finput = input(
            """ --  DECODING / ENCODING  --
            For decode/rozkoduj press 'd' or 'D'.
            for encode/zakoduj press 'e' or 'E'.
            My choice:  """
            ).lower()
        print(finput)

        if finput == 'd' or finput == 'e':
            pass
        else:
            rozko_zako()

    except ValueError:
        print('Not a good value')
        rozko_zako()

    li = inputowanie()  # tuple / list
    lista = []
    dzialanie = int
    try:
        for elem in li[0]:
            if finput == 'd':
                dzialanie = int(-li[1])
            elif finput == 'e':
                dzialanie = int(li[1])
            else:
                print('wrong input')
                rozko_zako()

            elem2 = int(ord(elem)) + dzialanie
            lista.append(elem2)
    except ValueError:
        print('Not a good value')
        rozko_zako()

    lista2 = []
    ret = ''
    for i in lista:
        i = chr(i)
        lista2.append(i)
        ret = ''.join(str(t) for t in lista2)
    print('wynik: ', ret)


def inputowanie():  # wersja1
    list_inp = []
    tekst1 = input('Wpisz tekst:  ') or ''
    tekst2 = input('Klucz szyfrowania:  ') or 3
    list_inp = [tekst1, tekst2]
    return list_inp  # list


# def inputowanie():   # wersja2
#     tekst1 = input('Wpisz tekst:  ') or ''
#     tekst2 = input('Klucz szyfrowania:  ') or 3
#     return tekst1, tekst2  # tuple

rozko_zako()
