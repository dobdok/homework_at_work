"""
do napisania program przypominający działaniem listę TODO
aplikacja do przechowywania zadań wraz ze stanami - TODO, IN PROGRESS, DONE

aplikacja powinna
    wyświetlać aktualne zadania - można użyć zewnętrznej biblioteki do "rysowania" tabeli
    dać możliwość dodawania nowych zadań
    dać możliwość edytowania aktualnych zadań
    dać możliwość usuwania istniejących zadań
    zapisywanie stanu do pliku przy kończeniu pracy
    pobieranie stanu z pliku przy uruchomieniu aplikacji
    dodać menu mówiące użytkownikowi w jakim miejscu się znajduje/ co wykonuje
    budowa aplikacji powinna być przemyślana, aplikacja powinna być rozbita na kilka mniejszych modułów / pakietów
        wykorzystać poznane elementy języka Python
        wykorzystać klasy do modelowania danych
"""



# from tabulate import tabulate

# jakie dzialanie, dodanie, usuniecie, edit etc
# wybor kolumny

def add_to_dict(wyniki):
    dict_all = {
        "TODO": [],
        "IN PROGRESS": [],
        "zadania_done": []
        }

    input_where = where_modify()
    if input_where == "T":
        dict_all["TODO"].append(wyniki)
    if input_where == "I":
        dict_all["IN PROGRESS"].append(wyniki)
    if input_where == "D":
        dict_all["zadania_done"].append(wyniki)
    print(dict_all)

def inputs():
    my_list = []
    id = 0
    #  here adding the data to TO DO list
    while True:
        id += 1
        data = input(f"enter your data:  ")
        indeksowane_data = "ID_" + str(id) + " " + data   # nadanie inputowi indeksu
        print(indeksowane_data)
        my_list.append(indeksowane_data)
        # print(my_list)
        add_to_dict(my_list)



def where_modify():
    where_modify_inp = input('where to edit todo, in progress, zadania_done').upper()
    return where_modify_inp



# def dictionaries():
#     while True:
#         wejsciowe = inputs()
#         dict_all = {
#             "TODO": [wejsciowe],
#             "IN PROGRESS": [wejsciowe],
#             "zadania_done": [wejsciowe]
#             }
#     return dict_all
# dictionaries()

# def remove():
#
#     my_list = []
#     id = 0
#     while True:
#         id += 1
#         data = input(f"enter your data:  ")
#         # nadanie inputowi indeksu
#         indeksowane_data = "ID_" + str(id) + " " + data
#         print(indeksowane_data)
#         my_list.append(indeksowane_data)
#         print(my_list)
#         return my_list

# mydict_todo = {"TODO":inputs()}
# print(mydict_todo)
#
# mydict_in_progress = {"IN PROGRESS":inputs()}
# print(mydict_in_progress)
#
# mydict_done = {"zadania_done":inputs()}
# print(mydict_done)


#
#
#
# mydict = {
#     "TODO": ["ID_11 Alice", "ID_111 Bob", "ID_105 Alan", "ID_055 Max"],
#     "IN PROGRESS": [],
#     "zadania_done": ["ID_53 24"]
#     }
#
#
#

# mydict2 = [mydict_todo, mydict_in_progress, mydict_done]
# print(tabulate(mydict, headers="keys", tablefmt="rounded_grid"))

#
# # print(mydict["TODO"][0], mydict["TODO"][2] )
# # print(mydict["TODO"][:], mydict["TODO"][2] )
#
#
# def search_index():
#
#     id = '11'
#     finded = (f'\n{[s for s in mydict["TODO"][:] if "ID_" + id + " " in s]}')
#     print(finded)
#     return finded
#
#
# search_index()
