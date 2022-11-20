'''
Progam w którym użytkownik:
1) Dodaje definicje
2) Szuka istniejących definicji
3) Usuwa wybrane przez niego definicje
'''

Words = {}

while(True):

    print("1. Dodaj definicję")
    print("2. Szukaj definicji:")
    print("3. Usun wybraną definicję:")
    print("4. Zakończ")

    choose = input('Wybierz opcje: ')

    if choose == '1':

        keyWord = input("Podaj klucz: ")
        defWord = input("Podaj definicję: ")
        Words[keyWord] = defWord
        print("Definicja została dodana\n")

    elif choose == '2':

        keyWord = input("Czego szukasz: ")

        if keyWord in Words:
            print(Words[keyWord], "\n")
        else:
            print("Nie znaleziono\n")

    elif choose == '3':

        keyWord = input("Co chcesz usunąć")

        if keyWord in Words:
            del Words[keyWord]
            print("Usunięto\n")
        else:
            print("Nie znaleziono\n")

    elif choose == '4':
        print("Zamykam\n")
        break

    else:
        print("Zły wybór, jeszcze raz\n")