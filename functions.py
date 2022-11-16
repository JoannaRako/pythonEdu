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

# dzielenie

def dzielenie (a, b) :
    if (b == 0) :
        return              # zwraca none
    print("Test: ")
    return a / b

x = dzielenie(10, 0)

if (x):      # False
    print("Tak")
else:
    print("Nie")

