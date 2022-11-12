#dictionary - słownik KLUC - WARTOŚĆ

pokoje = {49: 'Arkadiusz włodarczyk', 69: 'Wioletta włodarczyk'}
domy = {1: 'duzy', 2: 'maly'}

dane = {'imie': "Arkadiusz", 'nazwisko': "Włodarczyka"}

'''
wyszukiwanie:
>>> dane['imie']
'Arkadiusz'
lub
>>> dane.get('imie')
'Arkadiusz'

dodawanie:
>>> pokoje.update({400: 'Jan Kowalski'})

usuwanie:
>>> del(pokoje[555])
>>> pokoje.pop(400)
>>> pokoje.popitem() usuwa ostatni element i go zwraca
'''

pokoje[555] = 'ktos tam'