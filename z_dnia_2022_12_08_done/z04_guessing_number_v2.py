# zadanie 4:
# zgadywanie liczby
#     • program ma zaszytą w pamięci liczbę (może być stała, może być losowa)
#     • pyta użytkownika o zgadnięcie liczby
#     • kończy działanie programu gdy użytkownik zgadnie liczbę
#     • jeżeli użytkownik nie zgadnie liczby w 3 próbach, program daje podpowiedzi w postaci, liczba do zgadnięcia jest większa/mniejsza niż ta co podałeś

import random


def guessing_number():

    user_input = 0
    randomint = random.randint(1, 15)
    while user_input == int:
        user_input = input('Guess the Number between 1 and 15.\n   My Number is:  ')

    print(randomint)

    if randomint == user_input:
        print('You guessed corretly!')

    elif randomint != user_input:
        print('\nThe Number is incorrect. Please try again. ')
        user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))

        while randomint != user_input:
            print('\nThe Number is incorrect. Please try again.')
            user_input = input('Guess the Number between 1 and 15.\n   My Number is:  ')
            if randomint == user_input:
                print('You guessed corretly!')

            elif randomint > int(user_input):
                print('\nThe Number is bigger.')
            else:
                print('\nThe Number is smaller.')

    elif randomint == user_input:
        print('You guessed corretly!')
    else:
        print('Something went wrong. Start again.')

    print('The Number was: ', randomint)


guessing_number()
