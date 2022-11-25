def sumArguments(*arg):
    sum = 0

    for elements in arg:
        sum += elements
    return sum

print(sumArguments(2,4,5,6,7,8))

