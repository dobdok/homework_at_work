"""
# zadanie 1:
# algorytm sortowania bąbelkowego - zapoznać sie z zaimplementować
# program wczytuje od użytkownika dowolną liczbę liczb i sortuje je z użyciem algorytmu sortowania bąbelkowego
"""


def bubble_sorting():
    print('----- Bubble sorter -----')
    inputted_list = input('Enter list of numbers seperated by commas:  ')

    list_inputs = inputted_list.split(',')
    number_of_items = int(len(list_inputs))

    print(list_inputs)
    if type(number_of_items) == int:
        position = 0
        level = 0
        counter_1 = 1
        while counter_1 == 1:
            number_of_swaps = 1
            counter_2 = 0
            permanent_numbers = []
            while number_of_swaps > 0:
                counter_2 = counter_2 + 1
                number_of_swaps = 0
                while position < number_of_items - 1:
                    if int(list_inputs[position]) > int(list_inputs[position + 1]):
                        number_of_swaps = number_of_swaps + 1
                        item1 = int(list_inputs[position])
                        item2 = int(list_inputs[position + 1])
                        list_inputs[position] = item2
                        list_inputs[position + 1] = item1
                    position = position + 1
                level = level + 1
                # print('pass', level, ':', list_inputs)
                position = 0
                if level == number_of_items - 1:
                    number_of_swaps = 0
                permanent_numbers.append(int(list_inputs[number_of_items - counter_2]))
            if number_of_swaps == 0:
                counter_1 = 0


bubble_sorting()
