import calculationsModule

# enumeration - spis - wyliczenie

from enum import IntEnum

Menu = IntEnum('Menu', 'Prostokąt Kwadrat Trójkąt Trapez Koło')

# Menu = IntEnum('Menu', 'Prostokąt, Kwadrat, Trójkąt, Trapez, Koło')
# Menu = IntEnum('Menu', ['Prostokąt', 'Kwadrat', 'Trójkąt', 'Trapez', 'Koło'])
# Menu = IntEnum('Menu', {'Prostokąt':11, 'Kwadrat':12, 'Trójkąt':13, 'Trapez':14, 'Koło':15]}

# jak korzystasz z enumeracji zmienne z duzych liter


choose = int(input("""Wybierz pole której figury chcesz obliczyć?
                1. Prostokąt
                2. Kwadrat
                3. Trójkąt
                4. Trapez
                5. Koło
                """))

'''
ALBO 
from enum import Enum
Enum + if (choose == Menu.Prostokąt.value):

ALBO
from enum import IntEnum
IntEnum + if (choose == Menu.Prostokąt
'''

if (choose == Menu.Prostokąt.value):

    a = float(input("Długość:\n"))
    b = float(input("Szerokość:\n"))

    print("Pole wynosi:", calculationsModule.pole_prostokata(a, b))

elif choose == Menu.Kwadrat:

    a = float(input("Długość boku:\n"))

    print("Pole wynosi:", calculationsModule.pole_kwadratu(a))

elif choose == Menu.Trójkąt:

    a = float(input("Długość podstawy:\n"))
    h = float(input("Wysokość:\n"))

    print("Pole wynosi:", calculationsModule.pole_trojkata(a, h))

elif choose == Menu.Trapez:

    a = float(input("Długość podstawy\n"))
    h = float(input("Wysokość\n"))
    b = float(input("Długość podstawy\n"))

    print("Pole wynosi:", calculationsModule.pole_trapezu(a, b, h))

elif choose == Menu.Koło:

    r = float(input("Wprowadź promień:\n"))
    print("Pole wynosi:", calculationsModule.pole_kola(r))

else:
    print("Nie rozumiem")