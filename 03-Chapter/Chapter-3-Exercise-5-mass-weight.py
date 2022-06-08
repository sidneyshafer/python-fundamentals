# Get object mass
mass = float(input('Enter the object\'s mass: '))

# Calculate weight
weight = mass * 9.8

# Display results
if weight > 500:
    print('The object is too heavy.')
elif weight < 100:
    print('The object is too light.')
else:
    print('The object is just right.')
