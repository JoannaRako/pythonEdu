# wyrażenie zbioru

names = {"Arkadiusz", "Wioletta", "karol", "bartłomiej", "Jakub"}

namesCapitalize = {
                   name.capitalize()
                   for name in names
                   if not name.startswith("B")
                   if not name.startswith('b')
                  }

print(namesCapitalize)