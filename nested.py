# Zagnieżdżone typy danych - obiekty w obiektach o podobnych typach

listaGosci =    {
                  ('Arkadiusz', 28, 'mężczyzma', 546663456),
                  ('Arkadia', 30, 'kobieta', 654646463),
                  ('ichDziecko', 8, 'niewiadomo', 65366546543)
                }

listaGosci2 =   {
                  ('Arkadiusz', 28, 'mężczyzma', 65366546543),
                  ('bvv', 4, 'mężczyzma', 65366546543),
                  ('fgbf', 354, 'kobieta', 65366546543),
                  ('bfg', 5, 'niewiadomo', 65366546543)
                }

listaGosci3 = listaGosci | listaGosci2    # obie listy - suma
print(listaGosci3)

listaGosci3 = listaGosci & listaGosci2    # koniunkcja
print(listaGosci3)

listaGosci.add(('Karol', 25, 'mężczyzna')) 
# in tuple we use .add

print(listaGosci)


for imie, wiek, plec, numer in listaGosci:
  print("Imie:", imie)
  print("Wiek:", wiek)
  print("Płeć:", plec)
  print("Numer:", numer)
  print() # też enter


# dodawanie wartosci jest szybsze w slowniku, nie liczy sie kolejnosc

# dictionaries in dictionary

people = {
        "jdhIhjojJIojiOJIJuh1": { 'name': 'John', 'age': 27, 'sex': 'Male' },
        "54hgfjojJIoji67565h2": { 'name': 'Ben', 'age': 24, 'sex': 'Male' },
        "jdhIhjojJIojiOJIJuh3": { 'name': 'Ren', 'age': 76, 'sex': 'Female' },
        "544456nhhj54iOJIJuh4": { 'name': 'Ted', 'age': 85, 'sex': 'Male' },
        "fdgfhjojJIojiOJIJuh5": { 'name': 'Ross', 'age': 34, 'sex': 'Male' },
        "jahIgfdfdgfg44JIJuh6": { 'name': 'Monica', 'age': 56, 'sex': 'Female' },
        "ree67jojJIojiOJIJuh7": { 'name': 'Rachel', 'age': 54, 'sex': 'Female' }
         }

# list with dictionaries

peopleList = [
            {'id': 'gdfNJKHuUUUh', 'name': 'John', 'age': 27, 'sex': 'Male'},
            {'id': 'HUiuUIuUIUhg', 'name': 'Ben', 'age': 24, 'sex': 'Male'},
            {'id': '7vjuihykjkjh', 'name': 'Ren', 'age': 76, 'sex': 'Female'},
            {'id': 'ihuhJIJIJIJj', 'name': 'Ted', 'age': 85, 'sex': 'Male'},
            {'id': 'jiojijiojojU', 'name': 'Ross', 'age': 34, 'sex': 'Male'}
            ]

ratings =   {
            "Arkadiusz": (3, 3, 3, 4, 4, 5),
            "Beata": (3, 3, 3, 4, 4, 5),
            }

for key in ratings:           
    print (key, "oceny", ratings[key]) 

for dictionary in peopleList:         # dla kazdego rekordu w liscie
  for key in dictionary:              # i kazdego klucza w tym rekordzie
    print(key, dictionary[key])       # wydrukuj ktory to klucz i jego zawartosc
  print()


for key in people:
  print("id:", key)   # poszczególne klucze

  for dictionary in people[key]:
    print(dictionary, ":", people[key][dictionary])

  print()


for key in people:
    print("id:", key)   # poszczególne klucze

    for secondaryKey in people[key]:
        print(secondaryKey, ":", people[key][secondaryKey])

    print("\n")
'''
# metoda items - działa tylko dla słownika

# () - krotka
# [] - lista
# {} - słownik

print(people.items())

for id, dictionary in people.items():       # szybszy sposób
    print ("id:", id)
    for key in dictionary:
        print(key, ":", dictionary[key])