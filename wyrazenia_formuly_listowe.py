liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
            liczbyParzyste.append(element)

# szybsza wersja

potegiDwojki2 = [element**2 for element in liczby]

# można też napisać

potegiDwojki2 = [element**2                 # CO WYKONUJEMY
                 for elemenet in liczby     # SKĄD POBIERAMY
                ]

liczParzyste2 = [element                   # CO WYKONUJEMY - nic
                for element in liczby      # SKĄD POBIERAMY
                if (element % 2 == 0)      # WARUNEK
                ]
'''
co_zrobic_na_elemencie  for element in staraLista   warunek oparty na elemencie
'''