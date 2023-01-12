
"""# ------ zadania z dnia:  2022-12-08


# zadanie 1:
# konwerter minuty / godziny
#     • program pyta użytkownika o rodzaj konwersji
#     • prosi o podanie wartości do konwersji
#     • zwraca wynik
--done --


# zadanie 2:
# prosty kalkulator
#     • program prosi użytkownika o działanie jakie ma wykonać
#     • prosi o dwie liczby dla tego działania
#     • zwraca wynik
#     • program kończy swoje działanie dopiero na życzenie użytkownika a nie po zwróceniu wyniku
--done --


# zadanie 3:
# liczby parzyste
#     • program prosi o podanie liczby
#     • zwraca liczby parzyste większe od 0 do liczby podanej przez użytkownika (nie większe)
#     • podaje ile tych liczb jest
        # uwzględnić:
        # - zabezpieczenie przed nieodpowiednim wypelnieniem pola
        # - zabezpieczenie kiedy użytkownik pod nieparzystą
--done --


# zadanie 4:
# zgadywanie liczby
#     • program ma zaszytą w pamięci liczbę (może być stała, może być losowa)
#     • pyta użytkownika o zgadnięcie liczby
#     • kończy działanie programu gdy użytkownik zgadnie liczbę
#     • jeżeli użytkownik nie zgadnie liczby w 3 próbach, program daje podpowiedzi w postaci, liczba do zgadnięcia jest większa/mniejsza niż ta co podałeś
        # uwzględnić:
        # - zabezpieczenie przed nieodpowiednim wypelnieniem pola
        # - zminimalizować ilość kodu, napisane za dużo
--done --
"""




"""
# ------ zadania z dnia:  2022-12-15

# następne zadania zahaczą o materiał do list włącznie

# zadanie 1:
# algorytm sortowania bąbelkowego - zapoznać sie z zaimplementować
# program wczytuje od użytkownika dowolną liczbę liczb i sortuje je z użyciem algorytmu sortowania bąbelkowego
--TODO


# zadanie 2:
# totolotek
# program losuje 6 liczb od 1 do 49
# program prosi o wprowadzenie 6 liczb od 1 do 49 przez użytkownika
# program zwraca ilość "trafień"
--done --


# zadanie 3:
# kalkulator wag
# program przechowuje dane w postaci tablicy dwuwymiarowej
# program prosi o użytkownika o podanie dnia i wagi w danym dniu
# po zakończeniu wprowadzania danych (na życzenie używkonika) program wyświetla statystyki
# średnia, najwyższa i najniższa waga w każdym miesiącu (jeżeli brak danych dla konkretnego miesiąca to informacja o tym)
# średnia, najniższa, najwyższa waga w roku
--TODO
"""





"""
# ------ zadania z dnia:  2022-12-21

# zadanie 1:
# dzień roku
# napisz funkcję który jako parametr przyjmie rok i zwróci informację czy rok ten jest przestępny czy nie
# dodaj funkcję która jako parametr przyjmuje rok i miesiąc, a jako wynik zwraca informację ile dni jest w danym miesiącu
# napisz funkcję która 
        przyjmuje trzy parametry - rok, miesiąc i dzień, 
        sprawdzi czy wprowadzone dane są poprawne, 
        jeżeli nie zwróci wartość None, 
        jeżeli są poprawne zwróci informację który to dzień roku
--done -- 


# ------------

# zadanie 2:
# napisz funkcję która sprawdzi czy liczba jest pierwsza i zwróci wartość True lub False
--done --

# ------------

# zadanie 3:
# napisz funkcję obliczającą silnie, funkcja przyjmuje liczbę całkowitą i oblicza silnię dla niej + wersja rekurencyjna
--TODO

# ------------

# zadanie 4:
# funkcja obliczająca ciąg fibonacciego z wykorzystaniem rekurencji
--TODO

# ------------

# zadanie 5:
# napisz program który poprosi o wprowadzenie 
                                imienia studenta oraz 
                                oceny jaką uzyskał, 
                                "x" kończy wprowadzanie danych,
        po zakończeniu wprowadzania danych 
        zwraca średnią ocen dla każdego studenta oraz 
        dla całej klasy [słowniki do wykorzystania]
--TODO


# ------------

# zadanie 6:
# Napisz program/grę który będzie symulował wydostanie się z labiryntu
# program spyta o poziom trudności - łatwy/trudny
# program wylosuje labirynt na podstawie poziomu trudności
# poziom łatwy będzie miał 2 możliwości wyboru drogi (w każdym ruchu, np prawo/lewo)
# poziom łatwy będzie potrzebował 5 poprawnych ruchów do wyjścia z labiryntu
# poziom trudny będzie miał 2 albo 3 możliwości wyboru (losowanie dla każdego ruchu)
# poziom trudny będzie potrzebował 8 poprawnych ruchów do wyjścia z labiryntu
# niepoprawny ruch jest sygnalizowany użytkownikowi i pozostaje on na tym samym "poziomie"
# poprawny ruch jest sygnalizowany użytkownikowi i wyświetla się kolejny ruch
# program będzie liczył ilość ruchów użytkownika w labiryncie
# wyświetli statystyki:
# ile ruchów wykonał użytkownik
# jak była minimalna ilość ruchów aby wydostać się z labiryntu - dla 5 ruchów to oczywiście 5, dla 8 to 8
# jaka była maksymalna ilość ruchów aby wydostać się z labiryntu - dla poziomu łatwego to 10 (5 ruchów i jak zawsze pierwszy byłby zły to za 10 razem użytkownik by się wydostał, przyjmujemy że jak użytkownik dostanie informacje że wykonany ruch jest niepoprawny to już go nie powtórzy), dla poziomu trudnego maksymalna ilość ruchów jest zależna od wylosowania możliwości na każdym z ruchów
# jeżeli użytkownik przekroczył granice 60% ruchów pomiędzy minimalną wartością a maksymalną ruchów to gra kończy się niepowodzeniem, gracz umarł z głodu, np dla poziomu łatwego, min 5, max 10, 10 - 5 = 5, 60% z 5 = 3, 5 (min) + 3 (60%) = 8, jeżeli użytkownik w 8 ruchach nie wydostanie się to przegrywa, dla poziomu trudnego trzeba to liczyć w zależności od skomplikowania labiryntu
--TODO
"""



"""
# ------ zadania z dnia:  2023-01-05


# zadanie 1:
Napisz program, który będzie przypominał grę w kółko i krzyżyk

    program rysuje plansze do gry w kółko i krzyżyk
    komputer zaczyna rozgrywkę i wstawia "O" w dowolne pole
    program pyta użytkownika gdzie wstawić "X", użytkownik podaje dwie cyfry w formacie A B gdzie A to wiersz a B kolumna
    program sprawdza czy znak może być wprowadzony we wskazane pole
    program po każdym znaku rysuje aktualny układ planszy
    program po każdym znaku sprawdza czy ktoś nie wygrał rozgrywki
    program powtarza czynności do wykorzystania wszystkich pól
    skorzystaj z poznanych funkcji losujących aby program wybierał gdzie wstawić znak
    jeżeli nikt nie wygrał a skończyły się wolne pola, program informuje o tym użytkownika
--TODO
    

# ------------

# zadanie 2:
Napisać program program sprawdzający czy podany przez użytkownik ciąg znaków zawiera

    małe litery
    duże litery
    cyfry
    jeden ze znaków $#@
    minimum 6 znaków
    maksimum 12 znaków
--TODO

# ------------

# zadanie 3:
Napisać program który będzie działał na zasadzie Szyfru Cezara

    Program powinien spytać użytkownika o czynność którą chce wykonać - kodowanie / odkodowanie
    Spytać o wiadomość
    Spytać o punkt przesunięcia, jeżeli uzytkownik nic nie poda to przyjmie domyślną wartość - 3
    Wyświetlić zakodowany / odkodowany tekst
--done --

# ------------

# zadanie 4:
Napisz program, który będzie symulował zachowanie struktury danych typu "stos"

    do implementacji wykorzystaj podejście obiektowe
    stos musi przechowywać swój aktualny stan
    możemy dodawać elementy do stosu
    możemy pobierać elementy ze stosu
--TODO

# ------------

# zadanie 5:
Napisać program który

    posiada klasę Person (pola: imię, nazwisko, wiek, płeć, przeciążoną metodę __str__)
    posiada klasę Student (dziedziczy po klasie Person, dodatkowo zawiera pole z listą ocen i metodę do wyliczania średniej)
    posiada klasę Employee (dziedziczy po klasie Person, dodatkowo zawiera pole z informacją o zarobkach)
    każda klasa w osobnym pliku (module) i wykorzystać importowanie 
    w głównej klasie programu utworzyć listę minimum 10 obiektów po minimum jednej z każdej klasy
    wyświetlić tylko mężczyzn (z wygenerowanej listy - filter i lambda do użycia)
    wyświetlić studentów i średnią ich ocen
    wyświetlić pracowników i ich średnie zarobki
--TODO

przy implementacji zadań wykorzystać obsługę wyjątków w przypadku obsługi błędów (gdzie to potrzebne)

"""
