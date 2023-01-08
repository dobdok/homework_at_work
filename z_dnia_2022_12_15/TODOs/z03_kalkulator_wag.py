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
    > To close the program:  "Done".
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
                pass
                # to do the summary calculations
        else:
            print('It is not a correct value.')

    weight_l = []
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}
    while True:
        try:
            weight = float(input('Weight:  '))

            day = int(input('Day in month:  '))
            month = int(input('Month (number): '))
            year = int(input('Year:  '))

            # utworzyć listę, gdzie jeden element to będzie     day_l/month_l/year_l
            dates_l = []
            dates = f'Date: {str(year)}/{str(month)}/{str(day)}'

            weights = f'Weight: {str(weight)}'

            dates_l.append(dates)
            weight_l.append(weights)

            date_wage = {key: value for key, value in zip(dates_l, weight_l)}
            print('date_wage', date_wage)

            continue

        except ValueError:
            print('Please input numbers only.')
    print('date_wage', date_wage)


uinput()
