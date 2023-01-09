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
    welcometxt = """
    Keep dates and weight recorded.
    Type:
    > For input:  "I".
    > To see statistics:  "Sum".
    > To close the program (You can type it any time. Data then will be saved partially.):  "Done".
    Have a nice day!
    Type:  """
    usr_input = input(f'{welcometxt}')
    while True:
        try:

            if usr_input in usr_input:
                if usr_input == 'Done':
                    print('Program finished.')
                    quit()
                elif usr_input == 'I':
                    d_w_inputs()
                elif usr_input == 'Sum':
                    date_weight_sum()
                    # to do the summary calculations
                else:
                    uinput()
        except ValueError:
            print('Please input numbers only.')
            uinput()

    ###


def date_weight_sum():
    print('Summary:')

    output = d_w_inputs()
    print(output)

    # for i in d_w_inputs():
    #     print(i)

    # x = d_w_inputs()
    # print(x)

    # x = {d_w_inputs()}
    # print('x = {d_w_inputs}', x)
    # exit()


###

def d_w_inputs() -> dict:
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}
    date_weight_dict = {}
    date_l = []
    wei_l = []

    while True:
        try:
            weight = input('Weight:  ')
            if weight in weight:
                if weight == 'Done':
                    quit()
                elif weight == 'Sum':
                    date_weight_sum()
                elif (weight != 'Done' or weight != 'Sum') and int(weight) not in range(1, 9999):
                    print('It is not a correct value.')
                    continue
                elif (weight != 'Done' or weight != 'Sum') and type(int(weight)) == str:
                    print('It is not a correct value.')
                    continue

            else:
                print('It is not a correct value.')

            day = input('Day in month:  ')
            if day in day:
                if day == 'Done':
                    quit()
                elif day == 'Sum':
                    date_weight_sum()
                # elif int(day) > 31 or int(day) < 1:  # could be better TODO
                #     print('Please input numbers  between 1 and 31 only.')
                #     uinput()
                elif (day != 'Done' or day != 'Sum') and int(day) not in range(1, 32):
                    print('It is not a correct value.')
                    continue
            else:
                print('It is not a correct value.')

            month = input('Month (number): ')
            if month in month:
                if month == 'Done':
                    quit()
                elif month == 'Sum':
                    date_weight_sum()
                elif int(month) > 12 or int(month) < 1:
                    print('Please input numbers  between 1 and 31 only.')
                    uinput()

            year = input('Year:  ')
            if year in year:
                if year == 'Done':
                    quit()
                elif year == 'Sum':
                    date_weight_sum()

            dates = f'{str(year)}/{str(month)}/{str(day)}'

            weights = f'{str(weight)} kg'

            print(f'You added {dates} {weights}')

            date_l.append(dates)
            # print(date_l)
            wei_l.append(weights)
            # print(wei_l)
            date_weight_dict = {date_l[i]: wei_l[i] for i in range(len(date_l))}
            # print(date_weight_dict)
            # return date_weight_dict

        except ValueError:
            print('Please input numbers only.')
            uinput()


        print(date_weight_dict)
        return date_weight_dict


###
# d_w_inputs()


def run_program():
    uinput()
    d_w_inputs()


run_program()
