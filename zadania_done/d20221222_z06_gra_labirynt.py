"""
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
"""




import random

direction2 = ['l', 'r']
direction3 = ['l', 'r', 'u']


def input_level():
    print("""
    You are in the LABIRYNTH game. 
    In  the <EASY> game you have 5 moves to win the game. Your options are R for right or L for Left.
    In  the <HARD> game you have 8 moves to win the game. Your options are R for right or L for Left, U for Up.
    """)

    user_input_level = input('Type H for Hard or E for Easy:  ').lower()
    if user_input_level == 'e':
        easy()
    elif user_input_level == 'h':
        hard()





def easy():
    actual_position = 0
    all_moves = 0

    ostatni_ruch = True
    losowanie = str

    while actual_position < 5 and all_moves < 10:
        if ostatni_ruch:
            losowanie = random.choice(direction2)

        all_moves += 1
        user_input_move = input('Choose your move (R/L):  ').lower()
        if user_input_move == losowanie:
            print(f'\n>>>Good move You made {all_moves} move')
            ostatni_ruch = True
            actual_position += 1

        elif user_input_move != losowanie:
            print(f'Wrong move, Try again. You made {all_moves} move')
            ostatni_ruch = False

        if actual_position == 5:
            print('\n'+'* '*10)
            print(f"""
You Won!
You did {all_moves} moves.
Minimum moves is 5.""")


def hard():
    actual_position = 0
    all_moves = 0
    available_moves = 0
    good_moves = 0

    ostatni_ruch = True
    losowanie = str

    while actual_position < 8 and all_moves < 24:
        if ostatni_ruch:
            losowanie = random.choice(direction3)

        all_moves += 1
        user_input_move = input('Choose your move (R/L/U):  ').lower()
        if user_input_move == losowanie:
            good_moves +=1

            print(f"""\n>>>Good! {good_moves} good move.
You made {all_moves} moves.""")
            ostatni_ruch = True
            actual_position += 1

        elif user_input_move != losowanie:
            print(f'Wrong move, Try again. You made {all_moves} move')
            ostatni_ruch = False


        if actual_position == 5:
            print(f"""You Won!
You did {all_moves} moves.
Minimum moves is 8.""")




input_level()
