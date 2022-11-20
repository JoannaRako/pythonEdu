number = int(input("Wpisz liczbę do której mam sumować: \n"))

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

