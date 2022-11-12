"""
len() - długość - length
.append - dodać
.extend - rozszerzyć
.insert (index, co) - wstawić
.index - index danego elementu
sort (reverse=False) - sortuj rosnąco
max()
min()
.count - ile razy cos wystapi
.pop - usum ostatni elemen
.remove - usun pierwsze wystapienie
.clear - wyczysc liste
.reverse - zamien kolejnosc
"""


#
print("\nlen()")

lista1 = [1, 2, 3, 4]
lista2 = ["Arkadiusz", "Wioletta"]

print("długość listy:", len(lista1))


#
print("\n.append - doda na koncu wartosc na stale")

lista1 = [1, 2, 3, 4]
lista2 = ["Arkadiusz", "Wioletta"]

lista1.append(7)
print(lista1)

lista1.append([7, 8, 9, 0])
print(lista1)
#print(lista1 + [4]) - to nie zmienia zawartości


#
print("\n.extend")

lista1 = [1, 2, 3, 4]

lista1.extend([1, 2, 3, 4])
print(lista1)


#
print("\n.insert(index, co)")

lista1 = [1, 2, 3, 4, 54]
lista2 = ["Arkadiusz", "Wioletta"]

lista2.insert(0, "Kuba")
print(lista2)


#
print("\n.index")

print(lista1.index(3))
print(lista1.index(54))
print(lista2.index('Kuba'))


#
print("\nsort(reverse = False)")

unList = [43, 6, 6, 6, 3, 32, 23]
nmList = ["Arkadiusz", "Wioletta", "Cezary", "Makary"]

unList.sort()
print(unList)

unList.sort(reverse = True)
print(unList)

nmList.sort()
print(nmList)


#
print("\nmax()/min()")
unList = [43, 6, 6, 6, 3, 32, 23, -54, -654]

print(max(unList))
print(min(unList))


#
print("\n.count - ile razy coś wystąpi")

print(unList.count(6))
print(nmList.count("Arkadiusz"))


#
print("\n.pop()")

print(unList)

unList.pop()
print(unList)

unList.pop()
print(unList)


#
print("\n.remove()")

unList.remove(6)
print(unList)

unList.remove(3)
print(unList)

#
print(".reverse()")

unList.reverse()
print(unList)


#
print("\n.clear()")

unList.clear()
print(unList)



