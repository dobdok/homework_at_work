# zadanie 4:
# zgadywanie liczby
#     • program ma zaszytą w pamięci liczbę (może być stała, może być losowa)
#     • pyta użytkownika o zgadnięcie liczby
#     • kończy działanie programu gdy użytkownik zgadnie liczbę
#     • jeżeli użytkownik nie zgadnie liczby w 3 próbach, program daje podpowiedzi w postaci, liczba do zgadnięcia jest większa/mniejsza niż ta co podałeś

import random


def input_value():
    user_input = input('\nGuess the Number between 1 and 15.\n   My Number is:  ')

    try:
        if user_input.isdigit():
            return int(user_input)

        elif type(user_input) == str:
            print(f'The "{user_input}" is not an integer. Please repeat. \n')
            return input_value()

    except ValueError:
        print("That was definitely not integer nor string!")
        input_value()


def guessing_number():
    rint = random.randint(1, 15)
    print(rint)  # podgąd w celu weryfikacji

    value = 0

    while True:
        guessed_number = input_value()
        value += 1

        if guessed_number != rint and value <= 3:
            print('That is a wrong number, please guess again.')

        elif guessed_number > rint and value > 3:
            print('\nThe Number is smaller.')

        elif guessed_number < rint and value > 3:
            print('\nThe Number is bigger.')

        else:
            print('\nYou guessed corretly!')
            break


guessing_number()
