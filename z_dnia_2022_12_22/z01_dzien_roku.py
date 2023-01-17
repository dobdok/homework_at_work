"""# zadanie 1:
# dzień roku
# napisz funkcję która jako parametr przyjmie rok i zwróci informację czy rok ten jest przestępny czy nie

# dodaj funkcję która jako parametr przyjmuje rok i miesiąc, a jako wynik zwraca informację ile dni jest w danym miesiącu

# napisz funkcję która przyjmuje trzy parametry - rok, miesiąc i dzień, sprawdzi czy wprowadzone dane są poprawne, jeżeli nie zwróci wartość None, jeżeli są poprawne zwróci informację który to dzień roku"""


def czy_przestepny(rok):
    if rok % 4 == 0:
        if (rok % 100 != 0) and (rok % 400 == 0):
            return False  # nie jest przestępny
        else:
            return True  # jest przestępny
    else:
        return False


dane_testowe = [1900, 2000, 2016, 1987]
wyniki_testow = [False, True, True, False]
for i in range(len(dane_testowe)):
    r = dane_testowe[i]
    print(r, "->", end="")
    wynik = czy_przestepny(r)
    if wynik == wyniki_testow[i]:
        print("rok przestepny")
    else:
        print("Nie jest to rok przestepny")


###____________

def dni_w_miesiacu(rok, miesiac):
    if miesiac == 2 and (czy_przestepny(rok) == True): return 29
    if miesiac == 2 and (czy_przestepny(rok) == False): return 28
    # if (miesiac == 1 or miesiac == 3 or miesiac == 5 or miesiac ==  7 or miesiac == 8 or miesiac == 10 or miesiac == 12): return 31
    if miesiac in {1, 3, 5, 7, 8, 10, 12}: return 31
    # if miesiac == 4 or miesiac == 6 or miesiac == 9 or miesiac == 11: return 30
    if miesiac in {4, 6, 9, 11}:
        return 30
    else:
        return None


###____________

def dzien_w_roku(rok, miesiac, dzien):
    if dzien < 1: return None
    if miesiac in {1, 3, 5, 7, 8, 10, 12} and dzien > 31: return None
    if miesiac in {4, 6, 9, 11} and dzien > 30: return None
    rok_nie_przestepny = czy_przestepny(rok) == False
    rok_jest_przestepny = czy_przestepny(rok) == True
    if dni_w_miesiacu(rok, miesiac):
        if rok_jest_przestepny:
            if miesiac == 1: return dzien
            if miesiac == 2 and dzien > 29: return None
            if miesiac == 2: return 31 + dzien
            if miesiac == 3: return 31 + 29 + dzien
            if miesiac == 4: return 31 + 29 + 31 + dzien
            if miesiac == 5: return 31 + 29 + 31 + 30 + dzien
            if miesiac == 6: return 31 + 29 + 31 + 30 + 31 + dzien
            if miesiac == 7: return 31 + 29 + 31 + 30 + 31 + 30 + dzien
            if miesiac == 8: return 31 + 29 + 31 + 30 + 31 + 30 + 31 + dzien
            if miesiac == 9: return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + dzien
            if miesiac == 10: return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dzien
            if miesiac == 11: return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dzien
            if miesiac == 12: return 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dzien

        if rok_nie_przestepny:
            if miesiac == 1: return dzien
            if miesiac == 2 and dzien > 28: return None
            if miesiac == 2: return 31 + dzien
            if miesiac == 3: return 31 + 28 + dzien
            if miesiac == 4: return 31 + 28 + 31 + dzien
            if miesiac == 5: return 31 + 28 + 31 + 30 + dzien
            if miesiac == 6: return 31 + 28 + 31 + 30 + 31 + dzien
            if miesiac == 7: return 31 + 28 + 31 + 30 + 31 + 30 + dzien
            if miesiac == 8: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + dzien
            if miesiac == 9: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + dzien
            if miesiac == 10: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + dzien
            if miesiac == 11: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + dzien
            if miesiac == 12: return 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + dzien

    ###_______________________________


def test_dzien_w_roku():
    assert (dzien_w_roku(2000, 12, 31)) == 366
    assert (dzien_w_roku(2001, 12, 31)) == 365
    assert (dzien_w_roku(2001, 12, 32)) is None
    assert (dzien_w_roku(2016, 2, 30)) is None
    assert (dzien_w_roku(2016, 2, 29)) == 60
    assert (dzien_w_roku(2015, 2, 29)) is None
    assert (dzien_w_roku(2000, 12, 9)) == 344
    assert (dzien_w_roku(2016, 55, 7)) is None
    assert (dzien_w_roku(2000, 4, 4)) == 95
    assert (dzien_w_roku(2012, 2, 88)) is None
    assert (dzien_w_roku(1987, 1, 1)) == 1
    assert (dzien_w_roku(1987, 4, 31)) is None
    assert (dzien_w_roku(555, 1, 1)) == 1
    assert (dzien_w_roku(555, 1, 0)) is None


test_dzien_w_roku()
