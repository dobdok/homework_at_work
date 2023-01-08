# zadanie 3:
# liczby parzyste
#     • program prosi o podanie liczby
#     • zwraca liczby parzyste większe od 0 do liczby podanej przez użytkownika (nie większe)
#     • podaje ile tych liczb jest

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
    usr_input = input_value()

    while True:
        lp = 1
        if usr_input > 0 and usr_input % 2 == 0:
            even_numbers_list = []
            while lp <= usr_input:
                lp += 1
                if lp % 2 == 0:
                    even_numbers_list.append(lp)
            print('\nThe Even numbers above zero to the user input value: ', even_numbers_list)
            print('\nAmount of Even numbers: ', len(even_numbers_list))
            break
        elif usr_input % 2 != 0:
            print("\nTa liczba jest nieparzysta")
            even_numbers()
            break


even_numbers()
