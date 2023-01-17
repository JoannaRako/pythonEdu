import copy

def evil_function(toBeDestroyedList):
#   toBeDestroyedList.clear()
    print(id(toBeDestroyedList))
    toBeDestroyedList[0][0] = 20       # zmiana ID myList

myList = [[1, 4], [2, 1], [3, 6], [4, 2]]

print(id(myList))
evil_function(copy.deepcopy(myList))


# copy() - płytka
# evil_function(myList[:]) = copy / wycinek z listy od do

# deepcopy() - gleboka, np. listy w liscie => import copy
# jezeli sa obiekty mutable
