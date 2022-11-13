liczby = [1, 2, 3, 4, 5, 6]

potegiDwojki = []
for element in liczby:
    potegiDwojki.append(element**2)

liczbyParzyste = []
for element in liczby:
    if (element % 2 == 0):
            liczbyParzyste.append(element)

# szybsza wersja

potegi1 = [element**2 for element in liczby]

# można też napisać

potegi2 =   [element ** 2                 # CO WYKONUJEMY
            for element in liczby     # SKĄD POBIERAMY
            ]

parzyste2 = [element                   # CO WYKONUJEMY - nic
            for element in liczby      # SKĄD POBIERAMY
            if (element % 2 == 0)      # WARUNEK
            ]

'''
co_zrobic_na_elemencie  for element in staraLista   warunek oparty na elemencie
'''

liczby = [1, 2, 3, 4, 5, 6]

potegiRange = [element**2                   # CO WYKONUJEMY
              for element in range(20)     # SKĄD POBIERAMY
              ]

print(potegiRange)