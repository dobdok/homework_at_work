"""
# zadanie 6:
# Napisz program/grę który będzie symulował wydostanie się z labiryntu
# program spyta o poziom trudności - łatwy/trudny
# program wylosuje labirynt na podstawie poziomu trudności
#   poziom łatwy będzie miał 2 możliwości wyboru drogi (w każdym ruchu, np prawo/lewo)
#   poziom łatwy będzie potrzebował 5 poprawnych ruchów do wyjścia z labiryntu
#       poziom trudny będzie miał 2 albo 3 możliwości wyboru (losowanie dla każdego ruchu)
#       poziom trudny będzie potrzebował 8 poprawnych ruchów do wyjścia z labiryntu

# niepoprawny ruch jest sygnalizowany użytkownikowi i pozostaje on na tym samym "poziomie"
# poprawny ruch jest sygnalizowany użytkownikowi i wyświetla się kolejny ruch
# program będzie liczył ilość ruchów użytkownika w labiryncie


# wyświetli statystyki:
# ile ruchów wykonał użytkownik
# jak była minimalna ilość ruchów aby wydostać się z labiryntu - dla 5 ruchów to oczywiście 5, dla 8 to 8
# jaka była maksymalna ilość ruchów aby wydostać się z labiryntu - dla poziomu łatwego to 10 (5 ruchów i jak zawsze pierwszy byłby zły to za 10 razem użytkownik by się wydostał, przyjmujemy że jak użytkownik dostanie informacje że wykonany ruch jest niepoprawny to już go nie powtórzy), dla poziomu trudnego maksymalna ilość ruchów jest zależna od wylosowania możliwości na każdym z ruchów
# jeżeli użytkownik przekroczył granice 60% ruchów pomiędzy minimalną wartością a maksymalną ruchów to gra kończy się niepowodzeniem, gracz umarł z głodu, np dla poziomu łatwego, min 5, max 10, 10 - 5 = 5, 60% z 5 = 3, 5 (min) + 3 (60%) = 8, jeżeli użytkownik w 8 ruchach nie wydostanie się to przegrywa, dla poziomu trudnego trzeba to liczyć w zależności od skomplikowania labiryntu
"""
import random

direction2 = ['L', 'P']
direction3 = ['L', 'P', 'U']

print("""
You are in the LABIRYNTH game. 
In  the EASY game you have 5 moves to win the game. Your options are R for right or L for Left.

In  the HARD game you have 8 moves to win the game. Your options are R for right or L for Left, U for Up.
""")


def input_level():
    user_input_level = input('Type H for Hard and E for Easy:  ').lower()
    return user_input_level


game_level = input_level()

moves_all = 0  # actual position
moves_good = 0


def labirynth_definiowanie():
    ostatni_ruch = True
    while True:
        if game_level == 'e':
            labirynth2 = random.choice(direction2)
            labirynth3 = random.choice(direction3)
        easy_game = right_left_move()


            if easy_game == labirynth2:
                ostatni_ruch = True
                print('level easy ')
                if moves_good < 5 or moves_all < 11:  # jeszcze dobrze, gra trwa
                    pass
                elif moves_good == 5 or moves_all < 11:  # koniec, powód wygrana
                    print('')
                    pass
                elif moves_good < 5 or moves_all == 10:  # koniec, powód przegrana, za duzo ruchow
                    print('')
                    pass
                else:
                    ostatni_ruch = True








        if game_level == 'h':
            if easy_game == labirynth3:
                ostatni_ruch = False
                print('level easy ')

    #
    #     if ostatni ruch:
    #         choice
    #
    #     podanie ruchu
    #     if dobry:
    #         ostatni_ruch = True
    #     if zly:
    #         ostatni_ruch = False

    #     labirynth_list.append(labirynth)
    # elif game_level == 'h':
    #     for i in range(8):
    #         labirynth = random.choice(direction3)
    #         labirynth_list.append(labirynth)
    # print(labirynth_list)
    # return labirynth_list


def right_left_move():
    if game_level == 'e':
        user_input_move = input('Choose your move (R/L):  ').lower()
        print('e')


    elif game_level == 'h':
        user_input_move = input('Choose your move (R/L/U):  ').lower()
        print('h')

    if user_input_move == 'r':
        pass
    elif user_input_move == 'l':
        pass

    # return user_input_move


def run_labirynth():
    labirynth_definiowanie()
    right_left_move()


run_labirynth()
