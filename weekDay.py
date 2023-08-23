from enum import IntEnum

Menu = IntEnum("menu", "pn wt sr czw pt sb nd")

choose = int(input("""Wybierz dzień tygodnia,
                   poniedziałek
                   wtorek
                   sroda
                   czwartek
                   piątek
                   sobota
                   niedziela"""))

if (choose == menu.pn(a)):
    input("wppisz coś")

elif (choose == menu.wt):
    input("wppisz coś")

elif (choose == menu.sr):
    input("wppisz coś")

elif (choose == menu.czw):
    input("wppisz coś")

elif (choose == menu.pt):
    input("wppisz coś")

elif (choose == menu.sb):
    input("wppisz coś")

elif (choose == menu.nd):
    input("wppisz coś")

else:
    print("dziwny dzień tygodnia")