"""2022_12_08

zadanie 4:
zgadywanie liczby
    • program ma zaszytą w pamięci liczbę (może być stała, może być losowa)
    • pyta użytkownika o zgadnięcie liczby
    • kończy działanie programu gdy użytkownik zgadnie liczbę
    • jeżeli użytkownik nie zgadnie liczby w 3 próbach, program daje podpowiedzi w postaci, liczba do zgadnięcia jest większa/mniejsza niż ta co podałeś"""


import random


def guessing_number():
    randomint = random.randint(1, 15)
    print(randomint)
    while True:
        try:
            user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))

            if randomint == user_input:
                print('You guessed corretly!')
                break

            elif randomint != user_input:
                print('\nThe Number is incorrect. Please try again. ')
                user_input = int(input('Guess the Number between 1 and 15.\n   My Number is:  '))

                while randomint != user_input:
                    user_input = input('Guess the Number between 1 and 15.\n   My Number is:  ')

                    if randomint > int(user_input):
                        print('\nThe Number is bigger.')
                    else:
                        print('\nThe Number is smaller.')

                break
            else:
                print('Something went wrong. Start again.\n')

            print('The Number was: ', randomint)

        except ValueError:
            print("Please enter a valid integer 1-15\n")
            continue


guessing_number()
