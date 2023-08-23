import math

# WYBÓR:

choose = (input("Powierzchnię jakiej figury chcesz policzyć?\n"
                "1) prostokąta\n"
                "2) kwadratu\n"
                "3) trójkąta\n"
                "4) trapezu\n"
                "5) koła\n"))

# FUNKCJE:

def pole_prostokata(a, b):
    return a * b

def pole_kwadratu(a):
    return a * a

def pole_trojkata(a, h):
    return 0.5 * a * h

def pole_trapezu(a, b, h):

#   return 0.5 * a * h
    return (a + b) / 2 * h

def pole_kola(r):

    return math.pi * r ** 2


# OPCJA DO WYBORU:

if (choose == '1'):

    a = int(input("Długość:\n"))
    b = int(input("Szerokość:\n"))

    print(pole_prostokata(a, b))

elif choose == '2':

    a = int(input("Długość boku:\n"))

    print(pole_kwadratu(a))

elif choose == '3':

    a = int(input("Długość podstawy:\n"))
    h = int(input("Wysokość:\n"))

    print(pole_trojkata(a, h))

elif choose == '4':

    a = int(input("Długość podstawy\n"))
    h = int(input("Wysokość\n"))
    b = int(input("Długość podstawy\n"))

    print(pole_trapezu(a, b, h))

elif choose == '5':

    r = int(input("Wprowadź promień:\n"))
    print(pole_kola(r))

else:
    print("Nie rozumiem")



'''
# 1. Wersja rozszerzona
def sumUp(number):
    sum = 0
    for number in range(1, number+1):
        sum = sum + number
        print("Dla liczby", number, "Wartość sumowania to:", sum)
    print(sum)
sumUp(number)
'''

# 2. Pętlą
def sumUp_for(number):
    sum = 0

    for number in range(1, number+1):
        sum = sum + number
    return sum
print("2:", sumUp_for(number))


# 3. Wyrażeniem listy
def sumUp_generator(number):
    return sum([number for number in range(1, number+1)])
print("3:", sumUp_generator(number))


# 4. Wyrażeniem zbioru
def sumUp_generator(number):
    return sum((number for number in range(1, number+1)))
print("4:", sumUp_generator(number))


# 5. Wyrażeniem słownikowym
def sumUp_generator(number):
    return sum({number for number in range(1, number+1)})
print("5:", sumUp_generator(number))


# 6. Krótka wersja

def sumUp_short(number):
    return (1 + number) / 2 * number
print("6:", sumUp_short(number))

