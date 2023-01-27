# funkcja any(), by określić czy przesłana lista zawiera liczby parzyste

numbers1 = [1, 3, 5, 6, 7]
numbers2 = [1, 3, 5, 7, 9]


def any_even(lista):
    return any([number % 2 == 0 for number in lista])


print(any_even(numbers1))
print(any_even(numbers2))

if (any_even(numbers1)):
    print("Jest tam")
else:
    print("Nie ma")

if (any_even(numbers2)):
    print("Jest tam")
else:
    print("Nie ma")

# any - sprawdza czy JAKAKOLWIEK wartosc = True