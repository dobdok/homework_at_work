"""Napisać program który będzie działał na zasadzie Szyfru Cezara

    Program powinien spytać użytkownika o czynność którą chce wykonać - kodowanie / odkodowanie
    Spytać o wiadomość

    Spytać o punkt przesunięcia, jeżeli uzytkownik nic nie poda to przyjmie domyślną wartość - 3
    Wyświetlić zakodowany / odkodowany tekst


input1:
        rozkodowanie
        zakodowanie

input2:
        jaka wiadomosc



"""

print("""Choose option
c for code text
d for decode text""")


def firstInput():
    uinput1 = input("Type you choice of action?  ")

    if uinput1 == 'c' or uinput1 == 'C':
        function1()
        print('4')

    elif uinput1 == 'd' or uinput1 == 'D':
        function2()
        print('5')

    else:
        print('6')


def second_input():
    uinput2 = int(input("Type you choice of action?  ") or 3)
    return uinput2

    print(type(uinput2))

print(second_input())


def function1():
    print('1')
    user_message = input('Message text:')
    return user_message


def function2():
    print('2')


def funkcja3():
    firstInput()
    function1()
    print('3')


funkcja3()
