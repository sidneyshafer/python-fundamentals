# get number of square feet
square_feet = int(input('Enter the number of square feet: '))

# assign constant
ONE_ACRE = 43560

# divid number of square feet by acre to determine the number of acres per tract
acres = square_feet / ONE_ACRE

# print results
print('The number of acres is: ', acres)
