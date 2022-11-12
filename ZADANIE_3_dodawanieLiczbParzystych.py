"""
number = 0
sum = 0
i = 0

while i < 3:
    number = int(input("Wprowadź liczbę parzystą "))
    if number % 2 == 0 and number > 0:
        sum += number
    else:
        print("No ale miała być parzysta")
        continue
    i += 1

print("Twój wynik z tych parzystych liczb to:", sum)

"""

wynik = 0

i = 0

while i < 3:

    x = int(input("podaj dodatnie parzyste liczbę: "))

    if (x > 0 and not (x % 2)):

        wynik += x

    else:

        print("miała byc liczba dodatnia i parzysta, powtórz")

        continue

    i += 1

print("końcowy wynik", wynik)