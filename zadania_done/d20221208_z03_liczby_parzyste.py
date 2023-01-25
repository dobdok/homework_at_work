"""2022_12_08

zadanie 3:
liczby parzyste
    • program prosi o podanie liczby
    • zwraca liczby parzyste większe od 0 do liczby podanej przez użytkownika (nie większe)
    • podaje ile tych liczb jest
"""


def even_numbers():
    user_input = int(input('Please type the number (bigger than 0):  '))
    while True:
        lp = 1
        if user_input > 0 and user_input % 2 == 0:
            even_numbers_list = []
            while lp <= user_input:
                lp += 1
                if lp % 2 == 0:
                    even_numbers_list.append(lp)
            print('The Even numbers above zero to the user input value: ', even_numbers_list)
            print('Amount of Even numbers: ', len(even_numbers_list))
            break


even_numbers()


# do poprawy, 1.nieparzyste 2.napisac 2ga funkcje, uzyc petli for