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
