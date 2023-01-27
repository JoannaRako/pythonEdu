def double(x):
    return x * 2
print(double(4))

# to samo:
test = lambda x: x * 2
print(test(4))

# w skrócie
print((lambda x: x * 2)(4))

# można skorzystać na przykład w takiej sytuacji:
myList = [2, 14, 22, 7, 6, 4, 5, 17]

myList_filtered = list(filter(lambda x: x % 2 == 0, myList))
print(myList_filtered)

# wyrazeniowe
myList_filtered2 = [x for x in myList if (x % 2) == 0]
print(myList_filtered2)