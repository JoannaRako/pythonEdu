"""
#od 1 do 150

liczba = 0
while liczba <= 150:
        print (liczba)
        liczba += 1

# od 100 do 0

liczba = 100

while liczba >= 0:
    print (liczba)
    liczba -= 1
"""
#sumowanie

score = 0
i = 0

while i < 4:
    x = int(input("Podaj liczbe:"))
    print(x, "\n")
    score += x
    i += 1

print("Wynik dodawania tych liczb to:", score)