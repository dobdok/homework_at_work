# zadanie 2:
# totolotek
# program losuje 6 liczb od 1 do 49
# program prosi o wprowadzenie 6 liczb od 1 do 49 przez użytkownika
# program zwraca ilość "trafień"
from random import randint


def losy_programu():
    liczby = []
    count = 0
    while count <= 5:
        liczby.append(randint(1, 49))
        count += 1
    print('liczby', liczby)
    return liczby


def usr_inp():
    losy = losy_programu()

    inp1 = input('Type your first digit:  ')
    inp2 = input('Type your second digit:  ')
    inp3 = input('Type your third digit:  ')
    inp4 = input('Type your fourth digit:  ')
    inp5 = input('Type your fifth digit:  ')
    inp6 = input('Type your sixth digit:  ')

    inp_list = [int(inp1), int(inp2), int(inp3), int(inp4), int(inp5), int(inp6)]

    print('inp_list', inp_list, type(inp_list))
    print('losy', losy, type(losy))

    temp = set(inp_list)
    res = [i for i, val in enumerate(losy) if val in temp]

    print(f'The amount of matching elements : {len(res)}')


usr_inp()
