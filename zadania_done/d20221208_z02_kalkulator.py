"""2022_12_08

zadanie 2:
prosty kalkulator
    • program prosi użytkownika o działanie jakie ma wykonać
    • prosi o dwie liczby dla tego działania
    • zwraca wynik
    • program kończy swoje działanie dopiero na życzenie użytkownika a nie po zwróceniu wyniku
"""


def calculator():

    while True:
        user_choice = input(
            'What action do you want to perform?\n  If you want addition, type 1.\n  If you want subtraction, type 2.\n  If you want multiplication type 3.\n  If yopu want division, type 4.\nI want:  '
            )
        input_velue1 = float(input('Type please the first value:  '))
        input_velue2 = float(input('Type please the second value:  '))
        if user_choice == '1':
            print('The result: ', input_velue1 + input_velue2)
            print('- ' * 15, '\n')
        elif user_choice == '2':
            print('The result: ', input_velue1 - input_velue2)
            print('- ' * 15, '\n')
        elif user_choice == '3':
            print('The result: ', input_velue1 * input_velue2)
            print('- ' * 15, '\n')
        elif user_choice == '4':
            if input_velue2 == 0:
                print('You cannot divide by 0. Please type another value.')
                input_velue2 = float(input('Type please the second value:  '))
                print('The result: ', input_velue1 / input_velue2)
                print('- ' * 15, '\n')
            else:
                print('The result: ', input_velue1 / input_velue2)
                print('- ' * 15, '\n')

        else:
            print('Please choose the action from 1 to 4.')
            print('- ' * 15, '\n')


calculator()
