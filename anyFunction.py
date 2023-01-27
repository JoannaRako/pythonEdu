# funkcja any(), by określić czy przesłana lista zawiera liczby parzyste

numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]
numbers3 = [2, 4, 6, 8]


def any_even(lista):
    return any([number % 2 == 0 for number in lista])

def all_even(lista):
    return all([number % 2 == 0 for number in lista])

print("Funkcja any\n")
print(any_even(numbers1))
print(any_even(numbers2))

print("\nFunkcja all")
print(all_even(numbers1))
print(all_even(numbers3))

print("\nPętla")
if (any_even(numbers1)):
    print("Jest tam")
else:
    print("Nie ma")

if (any_even(numbers2)):
    print("Jest tam")
else:
    print("Nie ma")

# any - sprawdza czy JAKAKOLWIEK wartosc = True
# all - WSZYSTKIE


john = {
        'name' : 'John Doe',
        'age' : 30,
        'skills' : ['Python', 'JavaScript', 'C++']
}

jane = {
        'name' : 'Jane Smith',
        'age' : 25,
        'skills' : ['Python', 'Java']
}