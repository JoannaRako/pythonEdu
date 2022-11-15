# wyrażenia słownikowe

names = {"Ardkadiusz", "Wioletta", "Karol", "Bartłomiej", "Jakub"}
numbers = [1, 2, 3, 4, 5, 6]
celsius = {'t1': -20, 't2': -15, 't3': 0, 't4': 12, 't5': 24}

# różni się od wyrażenia listownego tym, że podajemy co ma się stać dla klucz i wartość

fahrenheit = {
    temperature: ((degrees * 9/5) + 32)
    for temperature, degrees in celsius.items()          # .items() - zmienia klucz/wartość w tuples
}

fahrenheit5 = {
    temperature: ((celsius * 9/5) + 32)
    for temperature, celsius in celsius.items()
    if celsius > -5
    if celsius < 20
}

print(fahrenheit)
print(fahrenheit5)

# -------------------------

multipliedNumbers = {
    number: number*number
    for number in numbers
}

powerOFNumbers = {
    number: number**number
    for number in numbers
}

print(multipliedNumbers)
print(powerOFNumbers)

# -------------------------

namesLength = {
    name: len(name)       # 1 - klucz; 2 - wart
    for name in names
}

'''
>>> namesLength
{'Wioletta': 8, 'Jakub': 5, 'Karol': 5, 'Bartłomiej': 10, 'Ardkadiusz': 10}
'''


namesLength2 = {
    name: len(name)       # 1 - klucz; 2 - wart
    for name in names
    if name.startswith("A")
}
print(namesLength2)

'''
>>> namesLength
{'Ardkadiusz': 10}
'''

# można też:
namesLength2 = {name: len(name) for name in names   if name.startswith("A")}
