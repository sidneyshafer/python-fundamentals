# get ending limit from user
print('This program displays a list of numbers')
print('(starting at 1) and their squares')
end = int(input('How high should I go? '))

#print table headings
print()
print('Number\tSquare')
print('--------------')

# print numbers and their squares
for number in range(1, end + 1):
    square = number**2
    print(number, '\t', square)


