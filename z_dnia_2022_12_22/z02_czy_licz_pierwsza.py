# zadanie 2:
# napisz funkcję która sprawdzi czy liczba jest pierwsza i zwróci wartość True lub False


def if_prime(number):
    for nr in range(2, number):
        if (number % nr) == 0:
            print('Not prime number')
            return False
    print('Prime number')
    return True


def test_if_prime():
    assert if_prime(2) is True
    assert if_prime(8) is False
    assert if_prime(9) is False
    assert if_prime(11) is True
    assert if_prime(13) is True


test_if_prime()
