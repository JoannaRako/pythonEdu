import copy

def evil_function(toBeDestroyedList):
#   toBeDestroyedList.clear()
    toBeDestroyedList[0][0] = 20       # zmiana ID myList

myList = [[1, 4], [2, 1], [3, 6], [4, 2]]

# copy, modyfikacja typu bezpieczny oryginał - COPY

evil_function(myList.copy())
evil_function(myList.deepcopy(myList))
