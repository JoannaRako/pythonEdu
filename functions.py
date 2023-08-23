'''
def nazwa_funkcji():
    instrukcje
    instrukcje

    nazwa_funkcji()
'''


def welcome(name):
    print("Cześć", name, "miło mi potać Cię w moim programie")

names = ["Arku", "Wiolu", "Bartku"]

for name in names:
    welcome(name)

# funkcja obliczająca pole prostokąta

def pole_prostokata(dlugosc, szerokosc):
    return dlugosc * szerokosc                               # zwraca czystą wartpść (wtedy ma typ)

print(pole_prostokata(6, 7))
print(5 * pole_prostokata(3, 4))

print("To jest Twoje pole prostokata:", pole_prostokata(10, 5))


#  3 WERSJE FUNKCJI DZIELENIA

def dzielenie (a, b) :
    if (b == 0) :
        return              # zwraca none
    print("Test: ")
    return a / b


if dzielenie(10,0):
    print("Podzielono poprawnie")
else:
    print("Coś poszło nie tak")
'''
 |
 |
\ /
'''
x = dzielenie(10, 0)
if (x):      # False
    print("Tak")
else:
    print("Nie")


#   !!!PASS!!!
def nic_nie_rob():
  pass  # instrukcja "pass" informuje, że funkcja nic nie robi

#   ZWRACANIE
#   Jedną z funkcji, która nic nie zwraca jest funkcja "print".

#1
def daj_liczbe():
    return 5
#2
def pokaz_liczbe():
    print(5)

# Funkcja z instrukcją "print" nie zwraca żadnej wartości
x = pokaz_liczbe()
print(x)
# wyświetli 5 (ponieważ 5 jest wyświetlane w funkcji pokaz_liczbe oraz
# !!! zaraz po tym None, bo gdy nic się zwraca to funkcja zwraca None !!!
