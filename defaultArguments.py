def increment(x, amount = 1):
    return x + amount

import time

# Zmienna do wszystkiego
number = int(input("Wpisz liczbę do której mam sumować: \n"))

# 1. Pętlą
def sumUp_for(number):
    sum = 0
    for number in range(1, number + 1):
        sum = sum + number
    return sum

# 2. Wyrażeniem listy
def sumUp_generatorL(number):
    return sum([number for number in range(1, number + 1)])

# 3. Wyrażeniem zbioru
def sumUp_generatorS(number):
    return sum((number for number in range(1, number + 1)))

# 4. Wyrażeniem słownikowym
def sumUp_generatorD(number):
    return sum({number for number in range(1, number + 1)})

# 5. Krótka wersja
def sumUp_short(number):
    return (1 + number) / 2 * number


"""
dzięki domyślnemu argumentowi jesteśmy w stanie rozwinąć funkcję,
która już istnieje o argument z wartością domyślną, przez co wszystkie
inne funkcje nadal działają.
"""

def function_performance(func, arg, how_many_times = 1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end-start)

    return sum


def show_message(message):
    print(message)


print(function_performance(sumUp_for, number, 25))
print(function_performance(sumUp_generatorL, number))
print(function_performance(sumUp_generatorS, number))
print(function_performance(sumUp_generatorD, number))
print(function_performance(sumUp_short, number))

