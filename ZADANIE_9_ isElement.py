import time


def function_performance(func, arg, how_many_times=1):
    sum = 0

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum


setContainer = {i for i in range(1000)}
listContainer = [i for i in range(1000)]

element = int(input("Wprowadź element który chcesz sprawdzić\n"))


def is_element_set(element):
    if element in setContainer:
        return True

def is_element_list(element):
    if element in listContainer:
        return True


print(is_element_list(element))

print(is_element_set(element))
