# zadanie 4:
# zgadywanie liczby
#     • program ma zaszytą w pamięci liczbę (może być stała, może być losowa)
#     • pyta użytkownika o zgadnięcie liczby
#     • kończy działanie programu gdy użytkownik zgadnie liczbę
#     • jeżeli użytkownik nie zgadnie liczby w 3 próbach --->>> użytkow nik przegrał

import random


def guessing_number():
    randomint = random.randint(1, 15)
    user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))
    print(randomint)
    if randomint == user_input:
        print('You guessed corretly!')

    elif randomint != user_input:
        print('\nThe Number is incorrect. Please try again. You have 2 more changes.')
        user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))
        if randomint == user_input:
            print('You guessed corretly!')

        elif randomint != user_input:
            print('\nThe Number is incorrect. Please try again. You have 1 more chance.')
            user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))
            if randomint == user_input:
                print('You guessed corretly!')

            elif randomint != user_input:
                print('\nThe Number is incorrect. You lost.')
    else:
        print('Something went wrong. Start again.')

    print('The Number was: ', randomint)


guessing_number()
