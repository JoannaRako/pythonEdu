import sys

# wczytywane są wszystkie dane jednocześnie
evenNumbers =   [element
                for element in range(400)
                if (element % 2 == 0)
                ]

# generator poszczególnych elementow - tworzy elementy po drodze
evenNumbersGenerator = (element
                        for element in range (400)
                        if (element % 2 == 0)
                        )

print(sys.getsizeof(evenNumbers))
print(sys.getsizeof(evenNumbersGenerator))

for item in evenNumbersGenerator:
    print(item)

print("Rozmiar: ",sys.getsizeof(evenNumbersGenerator))

# za kazdym razem gdy odwolamy sie do generatora na bierzaco wyrzuci wartosc
# gdy duze dane i nie jest potrzebne zeby je przechowac
