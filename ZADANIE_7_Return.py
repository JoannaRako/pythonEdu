import math

# WYBÓR

choose = (input("""
        Powierzchnię jakiej figury chcesz policzyć?
        1) prostokąta
        2) kwadratu
        3) trójkąta
        4) trapezu
        5) koła
"""))

# OPCJA

if choose == 1:

    print("Wprowadź długość i szerokość:\n")
    a = int(input("Długość: "))
    b = int(input("Szerokość: "))

    pole_prostokata(a, b)

elif choose == 2:

    print("Wprowadź długość boku:\n")
    a = int(input("Długość boku: "))

    pole_kwadratu(a)

elif choose == 3:

    print("Wprowadź długość podstawy i wysokość\n")
    a = int(input("Długość podstawy: "))
    h = int(input("Wysokość: "))

    pole_trojkata(a, h)

elif choose == 4:

    print("Wprowadź długość podstawy i wysokość lub długość podstawy \n")
    a = int(input())
    b = int(input())
    h = int(input())

    pole_trapezu(a, b, h)

elif choose == 5:

    r = int(input("Wprowadź promień: "))
    pole_kola(r)
else:
    print("Nie rozumiem")

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





