"""
# zadanie 5:
# napisz program który poprosi o wprowadzenie imienia studenta oraz oceny jaką uzyskał, "x" kończy wprowadzanie danych, po zakończeniu wprowadzania danych zwraca średnią ocen dla każdego studenta oraz dla całej klasy [słowniki do wykorzystania]

# wprowadz dane
# zakończ

# wyswietl
#       średnia ocen per student
#       średnia per klasa (przyjmujemy, że wszystkie inputy to ta sama klasa(grupa) )


"""


def uinput():
    welcometxt = """
    Input name and grade - type "c".
    For close - type "x".
    >> """
    usr_input = input(f'{welcometxt}')

    while True:
        try:

            if usr_input in usr_input:
                if usr_input == 'x':
                    print('Program finished.')
                    quit()
                if usr_input == 'c':
                    name_grade_inputs()
                elif type(usr_input) == str:
                    name_grade_inputs()
                else:
                    uinput()
        except ValueError:
            print('Please input numbers only.')
            uinput()


def name_grade_inputs():
    name_list = []
    grades_list = []
    mid = float

    while True:
        try:
            name = input('NAME:  ')
            grade = input('GRADE:  ')

            if name in name:
                name_list.append(name)
                print(name_list)
            elif name == 'x':
                quit()

            if grade in grade:
                grades_list.append(int(grade))
                print(grades_list)

                total = sum(grades_list)
                mid = total / len(grades_list)
                print(mid)
                continue

                #####################
        except ValueError:
            print('')

        print(f'Mid grades per students class:  {mid}.')
        quit()


def run_program():
    uinput()
    name_grade_inputs()


run_program()
