# zadanie 3:
# liczby parzyste
#     • program prosi o podanie liczby
#     • zwraca liczby parzyste większe od 0 do liczby podanej przez użytkownika (nie większe)
#     • podaje ile tych liczb jest
# do poprawy, 1.nieparzyste 2.napisac 2ga funkcje, uzyc petli for


def input_value():
    user_input = input('Please type the number (bigger than 0):  ')

    try:
        if user_input.isdigit():
            return int(user_input)

        elif type(user_input) == str:
            print(f'\nThe "{user_input}" is not an integer. Please repeat. \n')
            return input_value()

    except ValueError:
        print("\nThat was definitely not integer nor string!")
        input_value()


def even_numbers():
    while True:
        try:
            user_input = input_value()
            break
        except ValueError:
            print('Input digits only. Please repeat')
            even_numbers()
    if user_input % 2 == 0:
        print(f'You have {user_input // 2} even numbers within your number')

        for dig in range(2, user_input + 1, 2):
            print(dig)
    else:
        print('That is not a Number. Please repeat.')
        even_numbers()


even_numbers()
