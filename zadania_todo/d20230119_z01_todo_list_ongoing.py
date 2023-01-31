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

class Task:
    __count = 0

    def __init__(self, description, status):
        self.description = description
        self.status = status
        self.id = Task.incr() #python magic method to increment id for every task

    @classmethod
    def incr(cls): #python magic method to increment id for every task
        cls.__count += 1
        return cls.__count

    def describe(self):
        return f'{self.id} id {self.description}'
while True:
    text = input('Wpisz treść zadania:    ')
    column = input('Do jakiej kolumny dodać [t]odo/in [p]rogress/[d]one:  ').lower()
    if column == 't':
        column = 'TODO'
    if column == 'p':
        column = 'IN PROGRESS'
    if column == 'd':
        column = 'DONE'
    print(column)
        


    a = Task(description=text, status=column)
    slownik2 = {a.describe(): a.status}
    print('wyprintuj index:  ', a.describe()[0])
    print(type(a.describe()[0]))
    print(slownik2)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
# from tabulate import tabulate

# jakie dzialanie, dodanie, usuniecie, edit etc
# wybor kolumny

class Welcome:
    input("""Welcome in TO-DO LIST !
You can:
[S]earch Tasks
[E]dit
[A]dd Tasks
[D]elete Tasks
[Q]uit
Just type the letter in the brackets.
My action:  """)





class Task:
    __count = 0

    def __init__(self, description, status):
        self.description = description
        self.status = status
        self.id = Task.incr()  # python magic method to increment id for every task

    @classmethod
    def incr(cls):  # python magic method to increment id for every task
        cls.__count += 1
        return cls.__count

    def describe(self):
        return f'{self.id} id {self.description}'


text = input('moje zadanie  ')
column = input('jaka kolumna  ')
a = Task(description=text, status=column)


def dodawanie():
    while True:
        slownik2 = {a.describe(): a.status}
        # print('wyprintuj index:  ', a.describe()[0])
        # print(type(a.describe()[0]))
        # print(slownik2)
        # return {a.describe(): a.status}
        return metoda_zbiera(slownik2)


def metoda_zbiera(**kwargs):
    print(kwargs)


print(metoda_zbiera())

# print('dodawanie', dodawanie())
# print('slownik2', dodawanie())


#
# nr_index = input('type nr index ')
# for nr_index in a.describe()[0]:
#     print(a.describe()[1])


# def add_to_dict(wyniki):
#     dict_all = {
#         "TODO": [],
#         "IN PROGRESS": [],
#         "zadania_done": []
#         }
#
#     input_where = where_modify()
#     if input_where == "T":
#         dict_all["TODO"].append(wyniki)
#     if input_where == "I":
#         dict_all["IN PROGRESS"].append(wyniki)
#     if input_where == "D":
#         dict_all["zadania_done"].append(wyniki)
#     print(dict_all)
#
# def inputs():
#     my_list = []
#     id = 0
#     #  here adding the data to TO DO list
#     while True:
#         id += 1
#         data = input(f"enter your data:  ")
#         indeksowane_data = "ID_" + str(id) + " " + data   # nadanie inputowi indeksu
#         print(indeksowane_data)
#         my_list.append(indeksowane_data)
#         # print(my_list)
#         add_to_dict(my_list)
#
#
#
# def where_modify():
#     where_modify_inp = input('where to edit todo, in progress, zadania_done').upper()
#     return where_modify_inp


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
