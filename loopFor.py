"""
#----------------------------
score = 0

for i in range(0, 4):
    x = int(input("Podaj liczbe: "))
    score += x

print("Twój wynik to", score)
#----------------------------
score = 0

for i in [0, 1, 2]:
    x = int(input("Podaj liczbe: "))
    score += x

print("Twój wynik to", score)
#-----------------------------
score = 0

for i in range(10):
    x = int(input("Podaj liczbe: "))
    score += x

print("Twój wynik to", score)

#-----------------------------
score = 0

for i in "Tyle ile jest tu char'ow":
    x = int(input("Podaj liczbe: "))
    score += x
    print(i, ". ")

print("Twój wynik to", score)

"""
score = 0

for i in range(10):
    if(i % 2 == 0):
        print("Yas")
    else:
        print(1)