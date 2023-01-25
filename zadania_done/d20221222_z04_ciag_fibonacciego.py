# zadanie 4:
# funkcja obliczająca ciąg fibonacciego z wykorzystaniem rekurencji


def fibonacci(n):  # fibonacci & rekurencja
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
