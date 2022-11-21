import time

# Zmienna do wszystkiego
number = int(input("Wpisz liczbę do której mam sumować: \n"))

# 1. Pętlą
def sumUp_for(number):
    sum = 0
    for number in range(1, number+1):
        sum = sum + number
    return sum


# 2. Wyrażeniem listy
def sumUp_generatorL(number):
    return sum([number for number in range(1, number+1)])


# 3. Wyrażeniem zbioru
def sumUp_generatorS(number):
    return sum((number for number in range(1, number+1)))


# 4. Wyrażeniem słownikowym
def sumUp_generatorD(number):
    return sum({number for number in range(1, number+1)})


# 5. Krótka wersja
def sumUp_short(number):
    return (1 + number) / 2 * number


# Funkcja mierzenia czasu do porównania
'''
def time_count(start):
    end = time.perf_counter()
    return end-start
'''

#-------------------------------------------------------
'''
# 2. function_performance wywołuje inną funkcję
def function_performance(func):
    func()

# 3. funkcja zostaje wywołana
def show_message():
    print("Wiadomość")
    
# 1. przesłanie funkcji show_message do function_performance
function_performance(show_message)
'''

#-------------------------------------- z argumentem

# 2. function_performance wywołuje inną funkcję-argument oraz drugi argument
def function_performance(func, arg):
    start = time.perf_counter()
    func(arg)
    end = time.perf_counter()
    return end - start

# 3. funkcja zostaje wywołana - wydrukowanie argumentu
def show_message(message):
    print(message)

# 1. przesłanie funkcji-argumentu 'sumUp_for' oraz argumentu 'number' do function_performance
print(function_performance(sumUp_for, number))
print(function_performance(sumUp_generatorL, number))
print(function_performance(sumUp_generatorS, number))
print(function_performance(sumUp_generatorD, number))
print(function_performance(sumUp_short, number))
