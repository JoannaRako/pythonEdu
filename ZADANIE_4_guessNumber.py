secretNumber = 10
userAnswear = 0
tries = 0


while(secretNumber != userAnswear and tries < 4):
    userAnswear = int(input("Wprowadź tu liczbę zobaczymy czy zgadniesz..."))

    if(userAnswear < secretNumber):
        print("Your number is too less")
    elif(userAnswear > secretNumber):
        print("Your number is too large")
    elif(userAnswear == secretNumber):
        print("Your answear is correct!")
    else:
        print("What?!")

    tries += 1

if(tries < 4):
    print("Uhu!")
else:
    print("To much tries!")


