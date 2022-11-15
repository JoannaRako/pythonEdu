"""
>       #greater then
<       #less then
==      #equal to
!=      #not equal to
>=      #greater or equal
<=      #less then or equal

"""
'''
a = int(input())
b = 5
c = 6

if (a == b) :
    print(True)
    print("Yaas")
elif (a == c) :
    print(True)
    print("Still yaas")
else :
    print(False)
    print("nooo")
'''

print("Wybierz jakie działanie chcesz wykonać...")

wybor = input('''
1. mnożenie - *
2. dzielenie - / 
3. dodawanie - +
4. odejmowanie - -
5. modulo - %
6. potęgowanie - ^
''')
# MOJ KALKULATOR

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if (wybor == '*') :
    print("Twój wynik to: ", a * b)
elif (wybor == '/' and b != 0) :
    print("Twój wynik to: ", a / b)
elif (wybor == '+') :
    print("Twój wynik to: ", a + b)
elif (wybor == '-') :
    print("Twój wynik to: ", a - b)
elif (wybor == '%') :
    print("Twój wynik to: ", a % b)
elif (wybor == '^') :
    print("Twój wynik to: ", a ** b)
else :
    print("nooo")