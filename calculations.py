import calculationsModule

# print(calculationsModule.pole_kwadratu(4))

choose = input("""Wybierz pole której figury chcesz obliczyć?
                1. Prostokąt
                2. Kwadrat
                3. Trójkąt
                4. Trapez
                5. Koło
                """)

if (choose == '1'):

    a = float(input("Długość:\n"))
    b = float(input("Szerokość:\n"))

    print("Pole wynosi:", calculationsModule.pole_prostokata(a, b))

elif choose == '2':

    a = float(input("Długość boku:\n"))

    print("Pole wynosi:", calculationsModule.pole_kwadratu(a))

elif choose == '3':

    a = float(input("Długość podstawy:\n"))
    h = float(input("Wysokość:\n"))

    print("Pole wynosi:", calculationsModule.pole_trojkata(a, h))

elif choose == '4':

    a = float(input("Długość podstawy\n"))
    h = float(input("Wysokość\n"))
    b = float(input("Długość podstawy\n"))

    print("Pole wynosi:", calculationsModule.pole_trapezu(a, b, h))

elif choose == '5':

    r = float(input("Wprowadź promień:\n"))
    print("Pole wynosi:", calculationsModule.pole_kola(r))

else:
    print("Nie rozumiem")