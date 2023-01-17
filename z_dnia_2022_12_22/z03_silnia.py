# zadanie 3:
# napisz funkcję obliczającą silnie,
# funkcja przyjmuje liczbę całkowitą
# i oblicza silnię dla niej + wersja rekurencyjna


## ------------------- rekurencja

def silnia_reku(n):
    if n > 1:
        oblicz = n * silnia_reku(n - 1)  # rekurencja, silni odnosi się do siebie samej
        print(oblicz)
        return oblicz
    return 1


## ------------------- BEZ rekurencji

def silnia_no_reku(n):
    iteracja = 1
    for i in range(2, n + 1):
        iteracja *= i
    print('silnia_no_reku ->> ', iteracja)
    return iteracja


silnia_reku(5)
silnia_no_reku(5)
silnia_reku(20)
silnia_no_reku(20)
silnia_reku(3)
silnia_no_reku(3)



