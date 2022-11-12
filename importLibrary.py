liczba = 4

print("Import biblioteki:")
import math

math.sqrt(liczba)
print(liczba)

print("Import tylko jednej funkcji:")
from math import sqrt  # tylko ta funkcja z biblioteki

print(sqrt(liczba))

print("Import wszystkie funkcje z biblioteki:")
from math import *  # import wszystko

print(ceil(4.2))  # zaokragla do gory

# w konsoli po zaimportowaniu bibliotek rowniez mozna

print("Wartosc bezwzgledna")
drugaLiczba = -8
print(abs(drugaLiczba))  # wartosc bezwzgledna
