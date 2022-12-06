"""
Obiekt:
    immutable: bool, int, float, tuple, str
    mutable - zmienny
Do obiektów przypisane są metody

= - Zmiana miejsca wskazywania na nowy adres
"""

a = 4

print(a.bit_length())           # metoda

listSample = [1, 4, 513, 24]
print(id(listSample))

listSample2 = listSample
print(id(listSample))

listSample2.append(654)     # Doda do obu list wart. (to samo id)
print(id(listSample))

listSample[0] = 7
print(id(listSample))



a = 4
print(id(a))

b = a                   # obiekt immutable
print(id(b))

b = 7
print(id(b))


k = 4           # ten sam obiekt o tym samym adresie
h = 4           # ten sam obiekt o tym samym adresie



c = 5                       # to samo id
print(id(c))
def add(c, amount = 1):
    print(id(c))            # to samo id
    c = c + amount
    print(id(c))
add(c)




def append_el_to_list(listka, element):       # Placeholder
    print(id(listka))
    listka.append(element)
    print(id(listka))

print(id(listSample))
append_el_to_list(listSample, 5)       # przesyłać mutable zmiana zajdzie na oryginale

print(listSample)