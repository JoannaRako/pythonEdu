'''
Znajdz liczby od 100 do 470 włącznie, które są:
- podzielne prze 7, ale nie są podzielne przez 5

1) generator
2) wyrazenie listowne
3) wyrazenie zbioru
4) wyrazenie słownikowe

'''

# 1) generator

evenNumbersGenerator = (element
                        for element in range(100, 470)
                        if (element % 7 == 0)
                        if not (element % 5 == 0)
                        )

print("Generator:\n")
for item in evenNumbersGenerator:
    print(item)

# 2) wyrazenie listowne

listGenerator = [element
                for element in range(100, 470)
                if (element % 7 == 0)
                if not (element % 5 == 0)
                ]

print("Listowne:\n")
for item in listGenerator:
    print(item)

# 3) wyrazenie zbioru

setGenerator = {element
                for element in range(100, 470)
                if (element % 7 == 0)
                if not (element % 5 == 0)
                }

print("Zbioru:\n")          #
for item in setGenerator:
    print(item)

# 4) wyrazenie słownikowe


print("Słownik nie!\n")
