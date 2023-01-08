# zadanie 1:
# konwerter minuty / godziny
#     • program pyta użytkownika o rodzaj konwersji
#     • prosi o podanie wartości do konwersji
#     • zwraca wynik


import datetime


def convert_hours_minutes():
    while True:
        user_choice = input(
            'What do you want to convert?\n  Type 1 if you want convert min to hours.\n  Type 2 if you want convert hours to min.\nI want:  '
            )

        if user_choice == '1':
            print('You picked min to hours.\n', '-' * 20)
            minutes_amount = float(input('Type amount (in minutes):  '))
            print(minutes_amount / 60, 'hours')
            break

        elif user_choice == '2':
            print('You picked hours to min.\n', '-' * 20)
            hours_amount = float(input('Type amount (in hours):  '))
            print(hours_amount * 60.00, 'Minutes')
            break

        else:
            print('Type a number 1 or 2.\n', '-' * 20)


convert_hours_minutes()
