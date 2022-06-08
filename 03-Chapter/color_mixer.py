# Display primary colors to user
print('The primary colors are red, blue, and yellow')

# Get primary colors
p1 = input('Enter a primary color: ')
p2 = input('Enter ANOTHER primary color: ')

# Configure colors
if p1 == 'red' and p2 == 'blue':
    print('You made purple!')
elif p1 == 'blue' and p2 == 'red':
    print('You made purple!')
elif p1 == 'red' and p2 == 'yellow':
    print('You made orange!')
elif p1 == 'yellow' and p2 == 'red':
    print('You made orange!')
elif p1 == 'blue' and p2 == 'yellow':
    print('You made green!')
elif p1 == 'yellow' and p2 == 'blue':
    print('You made green!')
else:
    print('ERROR. You did not enter primary numbers')
