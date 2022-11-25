import time


# funkcja która sprawdzi jak szybko działa inna funkcja podaną lub domyślną ilość razy


def function_performance(func, how_many_times=1, **arg):
    sum = 0

    print(arg.get("what_value"))
    print(arg.get("container"))

    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(**arg)
        end = time.perf_counter()
        sum = sum + (end - start)

    return sum


setContainer = {i for i in range(10000)}
listContainer = [i for i in range(10000)]

element = int(input("Wprowadź element który chcesz sprawdzić\n"))


def is_element_in(what_value, container):
    if element in container:
        return True


# print(function_performance(is_element_in, element, setContainer, how_many_times = 20
# Jeżeli na odwrót nie trzeba odwoływać się do nazwy zmiennej
print(function_performance(is_element_in, 20, what_value=element, container=listContainer))

# ARGUMENTY POZYCYJNE (NIENAZWANE) PRZED ARGUMENTAMI NAZWANYMI
# *arg wiele arg nienazwanych(np. what_value = element, container = listContainer)
# **arg wiele arg nazwanych(np. what_value = element, container = listContainer)
