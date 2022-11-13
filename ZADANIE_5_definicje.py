'''
Progam w którym użytkownik:
1) Dodaje definicje
2) Szuka istniejących definicji
3) Usuwa wybrane przez niego definicje
'''

Words = {}

print("1. Dodaj definicję")
print("2. Szukaj definicji:")
print("3. Usun wybraną definicję:")
print("4. Zakończ")

choose = input('Wybierz opcje: ')

if (choose == 1):
    keyWord = input("Podaj klucz: ")
    defWord = input("Podaj definicję: ")
    Words[keyWord] = defWord
    print("Definicja została dodana")
'''
elsif (choose == 2):

elsif (choose == 3):

elsif (choose == 4):
    break
else :
    continue
'''