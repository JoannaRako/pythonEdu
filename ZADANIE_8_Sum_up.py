number = int(input("Wpisz liczbę do której mam sumować"))


def sumUp(number):
    sum = 0

    for number in range(1, number+1):

        sum = sum + number
        return sum

print(sumUp(number))