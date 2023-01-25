"""
Napisać program program sprawdzający czy podany przez użytkownik ciąg znaków zawiera

    małe litery
    duże litery
    cyfry
    jeden ze znaków $#@
    minimum 6 znaków
    maksimum 12 znaków

"""

import re

pat_lower = r'[\.a-z]'
pat_upper = r'[\.A-Z]'
digits = r'[\.0-9]'
other_ch = r'[\$\#\@]'


def znaki(check_str):
    print('\n', ('*' * 20))

    if re.search(pat_lower, check_str):
        print('ZAWIERA małe litery')
    else:
        print('nie ma małych liter')
        ###
    if re.search(pat_upper, check_str):
        print('ZAWIERA wielkie litery')
    else:
        print('nie ma wielkich liter')
        ###
    if re.search(digits, check_str):
        print('ZAWIERA cyfry')
    else:
        print('nie ma cyfr')
        ###
    if re.search(other_ch, check_str):
        print('ZAWIERA albo $ albo # albo @')
    else:
        print('nie ma ani $ ani # ani @')
        ###
    if len(check_str) >= 6:
        print('ZAWIERA 6 lub więcej znaków')
    else:
        print('znaków jest poniżej 6')
        ###
    if len(check_str) <= 12:
        print('ZAWIERA 12 lub mniej znaków.')
    else:
        print('znaków jest powyżej 12')

    print(f'\nZnaków w stringu: {len(check_str)}\n')


####

ciag_znakow1 = 'mnb LKH 34252 $#@'
ciag_znakow2 = 'mnb'
ciag_znakow3 = 'mnb @'
ciag_znakow4 = '4252 $#@'

znaki(ciag_znakow1)
print(ciag_znakow1)



znaki(ciag_znakow2)
print(ciag_znakow2)



znaki(ciag_znakow3)
print(ciag_znakow3)



znaki(ciag_znakow4)
print(ciag_znakow4)
