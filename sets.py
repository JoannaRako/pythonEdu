'''

    czy:    el.unikalne  | kolejnosc | zmiana konkret. el. | nowe el.
listy       NIE             TAK             TAK                 TAK
krotki      NIE             TAK             NIE                 NIE
słowniki    TAK             NIE             TAK                 TAK
zbiory      TAK             NIE             NIE                 TAK

'''

# zbiory nie mają kluczy tylko mają wartości
A = {1, 4, 20, -4, 20}
B = {2, 1, 25, 3, 20}

print(A)

A.add(7)
print(A)

A.discard(7)    # usuniecie ze zbioru

# żeby zmienić liste w ziór

lista = [1, 4, 4, 3, 6, 3333, 5]
print(set(lista))

print(A & B)        #  wspólna część
print(A | B)        # suma zbiory
print(A - B)        # odjecie zbioru wszystkie elem. A których nie ma w B
print(A ^ B)
''' ^ - xor, alternatywa wykluczajaca wyklucza wspól. wartości '''
print(A.issubset(B))    # czy A jest podzbiorem B
