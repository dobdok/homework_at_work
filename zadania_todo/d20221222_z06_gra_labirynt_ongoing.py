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


def input_easy_hard():
    user_input_hardness = input('Type H for Hard and E for Easy:  ').lower()
    return user_input_hardness

# def labirynth_easy():
#     labirynth_list = []
#     for i in range(5):
#
#         labirynth = random.choice(direction2)
#         labirynth_list.append(labirynth)
#     print (labirynth_list)
#     return labirynth_list
#
#
# def labirynth_hard():
#     labirynth_list = []
#
#     print(labirynth_list)
#     return labirynth_list
game_level = input_easy_hard()


def labirynth_definiowanie():
    labirynth_list = []
    if game_level == 'e':
        for i in range(5):
            labirynth = random.choice(direction2)
            labirynth_list.append(labirynth)
    elif game_level == 'h':
        for i in range(8):
            labirynth = random.choice(direction3)
            labirynth_list.append(labirynth)
    print(labirynth_list)
    return labirynth_list

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