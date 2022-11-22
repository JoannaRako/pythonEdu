import time

# funkcja która sprawdzi jak szybko działa inna funkcja podaną lub domyślną ilość razy


def function_performance(func, *arg, how_many_times = 1):

    sum = 0
    print(arg)

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum


setContainer = {i for i in range(10000)}
listContainer = [i for i in range(10000)]

element = int(input("Wprowadź element który chcesz sprawdzić\n"))


def is_element_in(element, container):
    if element in container:
        return True

print(function_performance(is_element_in, element, setContainer, how_many_times = 5))
print(function_performance(is_element_in, element, listContainer, how_many_times = 5))
