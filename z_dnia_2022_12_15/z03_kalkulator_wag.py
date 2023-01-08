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
    day_month = []
    day_l = []
    month_l = []
    weight_l = []
    year_l = []
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}

    welcometxt = """
    Keep dates and weight recorded.
    For input please type:  "I".
    To see statistics, input:  "Sum".
    To close the program, type:  "Done".
    Have a nice day!
    Type:  """


    while True:
        usr_input = input(welcometxt)
        if usr_input in usr_input:
            if usr_input == 'Done':
                print('Program finished.')
                quit()
            elif usr_input == 'I':
                pass
            elif usr_input == 'Sum':
                pass
                # to do the summary calculations
        else:
            print('It is not a correct value.')

    day_month = []
    day_l = []
    month_l = []
    weight_l = []
    year_l = []
    # utworzyć słownik, gdzie {day_l/month_l/year_l : weight_l}
    while True:
        try:
            weight = float(input('Input weight:  '))
            weight_l.append(weight)
            day = int(input('Input number of te day in month:  '))
            day_l.append(day)
            month = int(input('Input the number of the month?: '))
            month_l.append(month)
            year = int(input('Input the year?:  '))
            year_l.append(year)

            day_month[month][day][year] = weight
            break
        except ValueError:
            print('Please input numbers only.')


uinput()



















# def uinput():
#     slownik_wag_a_dat = {}
#
#     uinput = input('nr:  ')
#     while True:
#         if uinput == 'Done':
#             print('Done')
#         else:
#             isinstance(uinput, (int, float))
#             print('int or float')
#             return uinput

    # elif isinstance(uinput, (int, float)):
    #     print('int or float')
    # elif uinput == '3':
    #     pass
    # else:
    #     pass



# def check_user_input():
#     x = input('x:  ')
#     mlist = []
#
#     while True:
#         try:
#             # Convert it into integer
#             val = int(x) or float(x)
#             mlist.append(x)
#             return val
#         except ValueError:
#             try:
#                 val = "Done"
#                 mlist.append(x)
#                 return val
#             except ValueError:
#                 print("No.. input is not a number. It's a string")
#
#         break
#
#     print(mlist)


# check_user_input()
