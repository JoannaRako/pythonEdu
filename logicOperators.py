"""
and - && i
or - || lub
not - # if (not(a == 5 or b == 3))

"""

wart = int(input("Wpisz liczbe: "))

if (wart > 1 and wart < 10) :
    print("Dobrze wpisałeś")
else :
    print("Źle wpisałeś")

if (wart < 2 or wart > 10) :
    print("Dobrze wpisałeś")
else :
    print("Źle")