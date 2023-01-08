
# zadanie 6:
# Napisz program/grę który będzie symulował wydostanie się z labiryntu
# program spyta o poziom trudności - łatwy/trudny
# program wylosuje labirynt na podstawie poziomu trudności
# poziom łatwy będzie miał 2 możliwości wyboru drogi (w każdym ruchu, np prawo/lewo)
# poziom łatwy będzie potrzebował 5 poprawnych ruchów do wyjścia z labiryntu
# poziom trudny będzie miał 2 albo 3 możliwości wyboru (losowanie dla każdego ruchu)
# poziom trudny będzie potrzebował 8 poprawnych ruchów do wyjścia z labiryntu
# niepoprawny ruch jest sygnalizowany użytkownikowi i pozostaje on na tym samym "poziomie"
# poprawny ruch jest sygnalizowany użytkownikowi i wyświetla się kolejny ruch
# program będzie liczył ilość ruchów użytkownika w labiryncie
# wyświetli statystyki:
# ile ruchów wykonał użytkownik
# jak była minimalna ilość ruchów aby wydostać się z labiryntu - dla 5 ruchów to oczywiście 5, dla 8 to 8
# jaka była maksymalna ilość ruchów aby wydostać się z labiryntu - dla poziomu łatwego to 10 (5 ruchów i jak zawsze pierwszy byłby zły to za 10 razem użytkownik by się wydostał, przyjmujemy że jak użytkownik dostanie informacje że wykonany ruch jest niepoprawny to już go nie powtórzy), dla poziomu trudnego maksymalna ilość ruchów jest zależna od wylosowania możliwości na każdym z ruchów
# jeżeli użytkownik przekroczył granice 60% ruchów pomiędzy minimalną wartością a maksymalną ruchów to gra kończy się niepowodzeniem, gracz umarł z głodu, np dla poziomu łatwego, min 5, max 10, 10 - 5 = 5, 60% z 5 = 3, 5 (min) + 3 (60%) = 8, jeżeli użytkownik w 8 ruchach nie wydostanie się to przegrywa, dla poziomu trudnego trzeba to liczyć w zależności od skomplikowania labiryntu

