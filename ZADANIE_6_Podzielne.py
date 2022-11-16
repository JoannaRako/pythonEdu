'''
Znajdz liczby od 100 do 470 włącznie, które są:
- podzielne prze 7, ale nie są podzielne przez 5

1) generator
2) wyrazenie listowne
3) wyrazenie zbioru
4) wyrazenie słownikowe

'''

# wyrazenie listowne

evenNumbersGenerator = (element
                        for element in range (100, 400)
                        print(element)
                        if (element % 7 == 0)
                        if not element.endswith('0')
                        if not element.endswith('5')
                        )
print(evenNumbersGenerator)