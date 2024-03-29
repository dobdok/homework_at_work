"""
Napisz program, który będzie symulował zachowanie struktury danych typu "stos"

    do implementacji wykorzystaj podejście obiektowe
    stos musi przechowywać swój aktualny
    możemy dodawać elementy do stosu
    możemy pobierać elementy ze stosu

"""



class Stos:  # klasa elementu stosu
    def __init__(self, value=0, prev=None):
        self.v = value
        self.prev = prev


class Stos_all:
    def __init__(self):
        self.top = None

    def add(self, value):
        el = Stos(value, self.top)
        self.top = el

    def remove(self):  # pobieranie
        if self.top != None:
            self.top = self.top.prev
            print("Removed")

    def check(self):
        if self.top != None:
            return self.top.v
        return 'Empty'



    def if_empty(self):
        if self.top != None:
            return False
        print('It is empty.')
        return True



s = Stos_all()

## do some actions:

s.add(1)
print(s.check())

s.add(223)
print(s.check())

s.add(355)
print(s.check())

s.remove()
print(s.check())

s.remove()
print(s.check())

print("Is it empty? -> " + str(s.if_empty()))

s.remove()
print(s.check())
print("Is it empty? -> " + str(s.if_empty()))
