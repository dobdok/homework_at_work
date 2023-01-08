"""
# zadanie 1:
# algorytm sortowania bąbelkowego - zapoznać sie z zaimplementować
# program wczytuje od użytkownika dowolną liczbę liczb i sortuje je z użyciem algorytmu sortowania bąbelkowego
-----------------------------------------------------------------
# 1. wpisanie liczb
#       jedna po drugiej
#       kilku po kolei po przecinku i.e.  123, 123.5, 1.5

# 2. zakończenie wpisywania liczb wpisaniem jakiegoś tekstu/litery

# 3. pokazanie bąbelkowo posortowanych liczb

-----------------------------------------------------------------
--> jedna funkcja na wpisywanie&zakończenie liczb
--> druga funkcja na pokazanie bąbelkowo
"""
from os.path import split


def uinput():
    mlist = []

    user_input = input('\n11Number(s):  ')
    x = user_input.split(", ")

    while True:
        if user_input == "Done":
            break
        elif user_input != "Done":
            uinput()
            break
    mlist.append(user_input)





    print('22', mlist)


def babelki():
    print(
        '\nType a Number or Numbers separated by comma. If you want to type fractional numbers, use a dot as in 2.5 Number. You can type many Numbers as a one input, but you can also type each input separately (input + enter). When you are done, Please, type "Done." (without brackets).\nMy Number(s):  ')

    uinput()


babelki()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# def input_value1():
#     user_input = input('\n11Guess the Number between 1 and 15.\n   My Number is:  ')
#
#
#     try:
#         for i in user_input.split():
#             if isinstance(i, int):
#                 return user_input
#
#             elif isinstance(i, float):
#                 return user_input
#
#             else:
#                 print('Not Number, try again.')
#                 input_value1()
#     except ValueError:
#         print("That was definitely not integer nor string!")
#
#     # try:
#     #     if user_input.isdigit():
#     #         return int(user_input)
#     #
#     #     try:
#     #         x = float(user_input)
#     #     except ValueError:
#     #         print("You must enter a number")
#     #
#     #         if type(user_input) == str:
#     #             print(f'The "{user_input}" is not an integer. Please repeat. \n')
#     #             return input_value1()
#     #
#     # except ValueError:
#     #     print("That was definitely not integer nor string!")
#     #     input_value1()
#
#
# def input_value2():
#     user_input = input('\n22Guess the Number between 1 and 15.\n   My Number is:  ')
#     try:
#         for i in user_input.split():
#             if isinstance(i, int):
#                 return user_input
#
#             elif isinstance(i, float):
#                 return user_input
#
#             else:
#                 print('Not Number, try again.')
#                 input_value2()
#     except ValueError:
#         print("That was definitely not integer nor string!")
#
#
# def inputs():
#     mlist = []
#
#     # in1 = input('in 1')
#
#     # in2 = input('in 2')
#
#     count = 0
#     while True:
#         count += 1
#         if count == 1:
#             mlist.append(input_value1())
#
#         elif count > 0:
#             mlist.append(input_value2())
#
#
#
#         print('mlist:  ', mlist)
#
#
# inputs()
#
# # def usrinput():
# #     uinput = input('type number(s)')
# #     while True:
# #         if isDigit(uinput):
# #             user_list = uinput.split()
# #
# #             # print list
# #             print('list: ', user_list)
# #             return usrinput()
# #
# #
# #
# # usrinput()
#
# # def input_1st():
# #     user_input_first = input(
# #         '\nType a Number or Numbers separated by comma. If you want to type fractional numbers, use a dot as in 2.5 Number. You can type many Numbers as a one input, but you can also type each input separately (input + enter). When you are done, Please, type "Done." (without brackets).\nMy Number(s):  ')
# #
# #     while True:
# #         try:
# #             if isinstance(user_input_first, (int, float)):
# #                 return int(user_input_first)
# #
# #             elif type(user_input_first) == str:
# #                 print(f'The "{user_input_first}" is not an integer. Please repeat. \n')
# #                 return input_1st()
# #
# #         except ValueError:
# #             print("That was definitely not integer nor string!")
# #             input_1st()
# #
# # input_1st()
# # #
# # #
# # # def check_user_input():
# # #     list_numbers = []
# # #
# # #     finput = input(
# # #         '\nType a Number or Numbers separated by comma. If you want to type fractional numbers, use a dot as in 2.5 Number. You can type many Numbers as a one input, but you can also type each input separately (input + enter). When you are done, Please, type "Done." (without brackets).\nMy Number(s):  ')
# # #
# # #     sinput = input('Type another Number(s):  ')
# # #
# # #     count = 0
# # #     while True:
# # #         count += 1
# # #
# # #         # try:
# # #
# # #         if count == 0:
# # #             if type(finput) == int or type(finput) == float:
# # #                 return check_user_input()
# # #
# # #         if count > 0:
# # #             if (type(sinput) == int or type(sinput) == float) and count > 0:
# # #                 return check_user_input()
# # #
# # #         elif sinput == "Done.":
# # #             break
# # #
# # #         else:
# # #             print("Not a Number")
# # #             check_user_input()
# # #
# # #         # except ValueError:
# # #         #     print("No. The input is not a number.")
# # #         #     return check_user_input()
# # #
# # #     list_numbers.append(finput)
# # #
# # #     # elif finput == "Done.":
# # #     #     print("")
# # #
# # #     # print(list_numbers)
# # #
# # #
# # # check_user_input()
# # #
# # # #
# # # # def input_2nd():
# # # #     sinput = input('Type another Number(s):  ')
# # # #
# # # #
# # # # def input_value():
# # # #     list_numbers = []
# # # #     user_input_first = input(
# # # #         '\nType a Number or Numbers separated by comma. If you want to type fractional numbers, use a dot as in 2.5 Number. You can type many Numbers as a one input, but you can also type each input separately (input + enter). When you are done, Please, type "Done." (without brackets).\nMy Number(s):  ')
# # # #
# # # #
# # # #     while True:
# # # #         input = 0
# # # #         if input == 0:
# # # #
# # # #
# # # #
# # # #
# # # #     list_numbers.append(user_input)
# # # #     print(list_numbers)
# # # #     print(type(list_numbers))
# # # #     flag = True
# # # #
# # # #     try:
# # # #         for ch in user_input:
# # # #             ascii_code = ord(ch)
# # # #             if ascii_code > 57:
# # # #                 flag = False
# # # #                 break
# # # #
# # # #             if flag:
# # # #                 return list_numbers.append(user_input)
# # # #             else:
# # # #                 print(f'The "{user_input}" is not an integer. Please repeat. \n')
# # # #
# # # #     except ValueError:
# # # #         print("That was definitely not integer nor string!")
# # # #         input_value()
# # # #
# # # #     # print(type(user_input))
# # # #
# # # #     # list_numbers.append(user_input)
# # # #     # print(list_numbers)
# # # #     # print(type(list_numbers))
# # # #
# # # #     # try:
# # # #     #     if user_input.isdigit():
# # # #     #         return list_numbers.append(user_input)
# # # #     #
# # # #     #     if isinstance(user_input, list):
# # # #     #         return list_numbers.append(user_input)
# # # #     #
# # # #     #     elif type(user_input) == str and user_input != :
# # # #     #         print(f'The "{user_input}" is not an integer. Please repeat. \n')
# # # #     #         return list_numbers.append(user_input)
# # # #     #
# # # #     # except ValueError:
# # # #     #     print("That was definitely not integer nor string!")
# # # #     #     input_value()
# # # #
# # # #
# # # # input_value()
# # # #
# # # # # def sort_bablekowy():
# # # # #     pass
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # mlist = []
# # uinput = input("type: ")
# # mlist.append(uinput)
# #
# # while True:
# #
# #     list_of_numbers = []
# #     count = 0
# #     numbers = uinput.split()
# #     if count == 0:
# #         for n in numbers:
# #             list_of_numbers.append(n)
# #         print(list_of_numbers)
# #         break
# #     elif count > 0:
# #
# #
# #
# #
# #
# # # # lista = [7, 5, 3, 67, 0, 4, 12, 0]
# # # count_loops = 0
# # # while True:
# # #     for i in range(len(mlist)):
# # #         for j in range(len(mlist) - 1 - i):
# # #             print(count_loops)
# # #             count_loops += 1
# # #             if mlist[j] > mlist[j + 1]:
# # #                 mlist[j], mlist[j + 1] = mlist[j + 1], mlist[j]
# # #
# # #
# # # print(mlist)
# #
#
#
# #
# # def usrinput():
# #     mlist = []
# #     count = 0
# #     finput = input(
# #         '\nType a Number or Numbers separated by comma. If you want to type fractional numbers, use a dot as in 2.5 Number. You can type many Numbers as a one input, but you can also type each input separately (input + enter). When you are done, Please, type "Done." (without brackets).\nMy Number(s):  ')
# #
# #     sinput = input('Type another Number(s):  ')
# #
# #     while True:
# #         if isDigit(finput) and count == 0:
# #             count += 1
# #             mlist.append(finput)
# #             usrinput()
# #
# #         elif isDigit(sinput) and count > 0:
# #             count += 1
# #
# #             mlist.append(sinput)
# #             usrinput()
# #
# #     #
# #     # while count > 0:
# #     #     count += 1
# #     #     if isDigit(sinput):
# #     #         mlist.append(sinput)
# #     #         count += 1
# #     #         usrinput()
# #
# #     print(mlist)
# #
# #
# # #
# # # uinput = input("type: ")
# # # mlist.append(uinput)
# #
# #
# # usrinput()
