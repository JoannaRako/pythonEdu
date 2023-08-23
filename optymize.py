def addDefinition():
    key = input("Podaj klucz (słowo) do zdefiniowania: ")
    definition = input("Podaj definicję: ")
    definitions[key] = definition
    return "Definicja dodana pomyślnie"

def findDefinition():
    key = input("Czego szukasz? ")
    if key in definitions:
        return definitions[key]
    else:
        return "Nie znaleziono definicji o nazwie", key

def deleteDefinition():
    key = input("Jaką definicję chcesz usunąć? ")
    if key in definitions:
        del definitions[key]
        return "Usunięto definicję o nazwie:", key
    else:
        return "Nie znaleziono definicji o nazwie", key

def exitProgram():
    return "No to pa!"

def other():
    return "Podałeś coś z poza zakresu"


definitions = {}



while True:
    choose = input("Co chcesz zrobić?\n"
                   "1: Dodaj definicję\n"
                   "2: Znajdź definicję\n"
                   "3: Usuń definicję\n"
                   "4: Zakończ\n")


    if choose == "1":
        print(addDefinition())

    elif choose == "2":
        print(findDefinition())

    elif choose == "3":
        print(deleteDefinition())

    elif choose == "4":
        print(exitProgram())
        break

    else:
        print(other())