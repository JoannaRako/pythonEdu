import time

# Zmienna do wszystkiego
number = int(input("Wpisz liczbę do której mam sumować: \n"))

'''
# 1. Wersja rozszerzona
def sumUp(number):
    sum = 0
    for number in range(1, number+1):
        sum = sum + number
        print("Dla liczby", number, "Wartość sumowania to:", sum)
    print(sum)
'''

# 2. Pętlą
def sumUp_for(number):
    sum = 0
    for number in range(1, number+1):
        sum = sum + number
    return sum


# 3. Wyrażeniem listy
def sumUp_generator(number):
    return sum([number for number in range(1, number+1)])


# 4. Wyrażeniem zbioru
def sumUp_generator(number):
    return sum((number for number in range(1, number+1)))


# 5. Wyrażeniem słownikowym
def sumUp_generator(number):
    return sum({number for number in range(1, number+1)})


# 6. Krótka wersja
def sumUp_short(number):
    return (1 + number) / 2 * number

'''
start = time.perf_counter()
sumUp(number)
end = time.perf_counter()
print("Czas wykonania tej funkcji to: ", end-start)            # Odjęcie czasu początkowego od końcowego
'''

# Funkcja mierzenia czasu

def timeCount(start):
    end = time.perf_counter()
    return end-start

start = time.perf_counter()
print("2:", sumUp_for(number))
print(timeCount(start))


start = time.perf_counter()
print("3:", sumUp_generator(number))
print(timeCount(start))

start = time.perf_counter()
print("4:", sumUp_generator(number))
print(timeCount(start))


start = time.perf_counter()
print("5:", sumUp_generator(number))
print(timeCount(start))


start = time.perf_counter()
print("6:", sumUp_short(number))
print(timeCount(start))