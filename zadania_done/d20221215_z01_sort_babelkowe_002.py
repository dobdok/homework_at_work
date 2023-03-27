"""
# zadanie 1:
# algorytm sortowania bąbelkowego - zapoznać sie z zaimplementować
# program wczytuje od użytkownika dowolną liczbę liczb i sortuje je z użyciem algorytmu sortowania bąbelkowego
"""


def bubble_sorting():
    list_bubble = []

    length_list = 20
    while len(list_bubble) < length_list:
       try:
            number = int(input("\nInput the number: "))
            list_bubble.append(number)
       except ValueError:
           print('!! It should be number. ')

    print('Original value', list_bubble)



    i = 0
    while i < len(list_bubble) - 1:
        nr_elem = 0
        for nr_elem in range(len(list_bubble) - 1):
            if list_bubble[nr_elem] > list_bubble[nr_elem + 1]:
                list_bubble[nr_elem], list_bubble[nr_elem + 1] = list_bubble[nr_elem + 1], list_bubble[nr_elem]
            nr_elem += 1
        i += 1
    print('After Bubble soting', list_bubble)


bubble_sorting()
