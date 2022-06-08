TAX_FACTOR = 0.0065

# Get first lot number
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))

# proccess until 0 is entered
while lot != 0:
    value = float(input('Enter the property value: '))

# calculate property tax
tax = value * TAX_FACTOR

# display tax
print('Property tax: $', format(tax, ',.2f'), sep='')

# get next lot number
print('Enter the property lot number')
print('or enter 0 to end.')
lot = int(input('Lot number: '))
