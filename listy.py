"""
imiona = ["Arkadiusz", "Wioletta", "Karol"]
liczby = [1, 54, -2, 20]
mieszana = [1, 'a', 52]

for imie in imiona:
    print(imie)

print(imiona[-1])   # wybranie ostatniego elementu
print(imiona[3])

"""
#in

imiona = ["Arkadiusz", "Wioletta", "Karol", "Zuzia"]
liczby = [1, 54, -2, 20]

if("Wioletta" in imiona):   #sprawdza czy Wojtek jest w liscie imiona
    print("Jest tu takie imie")

#not in

if(4 not in liczby):
    print("Nie ma takiej liczby")
else:
    print("Jest")

#operacje na liczbach
print([3 * liczby])     #trzy razy ta lista

print([[4] + liczby])     #doda 4 na początek
print([liczby + [4]])     #doda 4 na koniec

liczby = [4] + liczby #przypisanie elementu do listy liczby

print(liczby)
