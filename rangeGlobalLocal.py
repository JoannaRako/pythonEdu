# W funkcji zmienna lokalna
def add():
    c = 5
    return c

# zmienna globalna
c = 1
print(c)

# w funkcji odwołanie do zmiennej globalnej
def add2():
    print(d)

d = 1
add2()


# w funkcji odwołanie do zmiennej globalnej ale przypisanie zmiennej lokalnej NIE ZADZIAŁA
def add33():
    e = e + 5
    print(e)

e = 1
add3()

# w funkcji odwołanie do zmiennej globalnej przypisanie zmiennej globalnej ZADZIAŁA
def add4():
    global f
    f = f + 5
    print(f)

f = 1
add4()

