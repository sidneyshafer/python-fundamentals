name1 = input('Enter a name (first name only): ')
name2 = input('Enter a second name (first name only): ')

print('Here are the names, listed alphabetically: ')

if name1 < name2:
    print(name1)
    print(name2)
else:
    print(name2)
    print(name1)
