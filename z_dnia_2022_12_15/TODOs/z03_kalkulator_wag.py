"""
# zadanie 3:
# kalkulator wag
# program przechowuje dane w postaci tablicy dwuwymiarowej
# program prosi o użytkownika o podanie dnia i wagi w danym dniu
# po zakończeniu wprowadzania danych (na życzenie używkonika) program wyświetla statystyki
#       średnia, najwyższa i najniższa waga w każdym miesiącu (jeżeli brak danych dla konkretnego miesiąca to informacja o tym)
#       średnia, najniższa, najwyższa waga w roku



1. input waga + data
        wielokrotnie
        na życzenie zakończenie

2. podsumowanie
       średnia, najwyższa i najniższa waga w każdym miesiącu
       informacja o braku danycnb dla miesiąca
       średnia, najniższa, najwyższa waga w roku
       example:

       Jan: 10 kg / 22.5 kg / 32 kg
       Feb:
       March:
       Apr:
       May: 30 kg / 100.8 kg / 236.7 kg
       June:
       July: no data
       Aug:
       Sep:
       Oct: no data
       Nov:
       Dec:
       2022: 1258.8 kg
"""


def uinput():
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}

    welcometxt = """
    Keep dates and weight recorded.
    Type:
    > For input:  "I".
    > To see statistics:  "Sum".
    > To close the program (You can type it any time. Data then will be saved partially.):  "Done".
    Have a nice day!
    Type:  """

    while True:
        usr_input = input(welcometxt)
        if usr_input in usr_input:
            if usr_input == 'Done':
                print('Program finished.')
                quit()
            elif usr_input == 'I':
                break
            elif usr_input == 'Sum':
                date_weight_sum()
                # to do the summary calculations
        else:
            print('It is not a correct value.')

    return usr_input

    ###


def date_weight_sum() -> int:
    x = 5
    if x == 5:
        print(x)  # to test if it works TODO
        exit()


###

def d_w_inputs():
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}
    mdict = {}
    while uinput():
        try:
            weight = input('Weight:  ')
            if weight in weight:
                if weight == 'Done':
                    quit()
                elif weight == 'Sum':
                    date_weight_sum()

            day = input('Day in month:  ')
            if day in day:
                if day == 'Done':
                    quit()
                elif day == 'Sum':
                    date_weight_sum()

            month = input('Month (number): ')
            if month in month:
                if month == 'Done':
                    quit()
                elif month == 'Sum':
                    date_weight_sum()

            year = input('Year:  ')
            if year in year:
                if year == 'Done':
                    quit()
                elif year == 'Sum':
                    date_weight_sum()

            # utworzyć listę, gdzie jeden element to będzie     day_l/month_l/year_l
            dates = f'{str(year)}/{str(month)}/{str(day)}'

            weights = f'{str(weight)} kg'


            mdict = {dates: weights}
            print(f'You added {dates} {weights}')
            continue

        except ValueError:
            print('Please input numbers only.')

    return mdict


###

def run_program():
    while d_w_inputs():
        mlist = [d_w_inputs()]
        print(mlist)


run_program()
