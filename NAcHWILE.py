# dodawanie wartosci jest szybsze w slowniku, nie liczy sie kolejnosc
# dictionaries in dictionary

people = {
          "jdhIhjojJIojiOJIJuh1":{ 'name': 'John', 'age': 27, 'sex': 'Male' },
          "jdhIhjojJIojiOJIJuh2":{ 'name': 'Ben', 'age': 24, 'sex': 'Male' },
          "jdhIhjojJIojiOJIJuh3":{ 'name': 'Ren', 'age': 76, 'sex': 'Female' },
          "jdhIhjojJIojiOJIJuh4":{ 'name': 'Ted', 'age': 85, 'sex': 'Male' },
          "jdhIhjojJIojiOJIJuh5":{ 'name': 'Ross', 'age': 34, 'sex': 'Male' },
          "jdhIhjojJIojiOJIJuh6":{ 'name': 'Monica', 'age': 56, 'sex': 'Female' },
          "jdhIhjojJIojiOJIJuh7":{ 'name': 'Rachel', 'age': 54, 'sex': 'Female' }
         }
'''
# list with dictionaries

peopleList = [
        {'id': 'gdfNJKHuUUUh', 'name': 'John', 'age': 27, 'sex': 'Male'},
        {'id': 'HUiuUIuUIUhg', 'name': 'Ben', 'age': 24, 'sex': 'Male'},
        {'id': '7vjuihykjkjh', 'name': 'Ren', 'age': 76, 'sex': 'Female'},
        {'id': 'ihuhJIJIJIJj', 'name': 'Ted', 'age': 85, 'sex': 'Male'},
        {'id': 'jiojijiojojU', 'name': 'Ross', 'age': 34, 'sex': 'Male'}
        ]

ratings = {
        "Arkadiusz": (3, 3, 3, 4, 4, 5),
        "Beata": (3, 3, 3, 4, 4, 5),
        }

for key in ratings:           
    print (key, "oceny", ratings[key]) 

for value in peopleList:
  for key in value:
    print(key, value[key])
  print()

'''

for key in people:
    print(key)
