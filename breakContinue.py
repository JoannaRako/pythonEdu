#break
"""
#tu break
score = 0

for i in range(3):
    x = int(input("Podaj dodatnia liczbe: "))
    if(x > 0):
        score += x
    else:
        print("No ale miala byc dodatnia")
        break #tutaj przerwie dzialanie
    print("Wynik dodawania dodatnich liczb: ", score)

score = 0
#tu continue
for i in range(3):
    x = int(input("Podaj dodatnia liczbe: "))
    if(x > 0):
        score += x
    else:
        print("No ale miala byc dodatnia")
        continue #tutaj przeskoczy i pojdzie dalej
    print("Wynik dodawania dodatnich liczb: ", score)
"""
#Jeżeli chcemy żeby nie przeskoczyło próby to pętla while
score = 0
i = 0

while i < 3:
    x = int(input("Podaj dodatnia liczbe: "))
    if (x > 0):
        score += x
    else:
        print("No ale miala byc dodatnia")
        continue  # tutaj pominie tą iteracje wgl
    i +=1

print("Wynik dodawania dodatnich liczb: ", score)

