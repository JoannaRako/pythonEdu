import sys

# wczytywane są wszystkie dane jednocześnie
evenNumbers =   [element
                for element in range(400)
                if (element % 2 == 0)
                ]

# generator poszczególnych elementow - tworzy elementy po drodze
evenNumbersGenerator = (element
                        for element in range (400)
                        if (element % 2 == 0)           # elementy parzyste
                        )

print("Rozmiar:", sys.getsizeof(evenNumbers))

for item in evenNumbersGenerator:
    print(item)

print("Rozmiar: ", sys.getsizeof(evenNumbersGenerator))

# za kazdym razem gdy odwołamy się do generatora na bieżąco wyrzuci wartość
# używane gdy duże dane i nie jest potrzebne żeby je przechować
