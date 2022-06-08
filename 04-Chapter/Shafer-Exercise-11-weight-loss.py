# Get user weight
weight = int(input('Enter your weight: '))

# Print table headings
print('Month\tWeight')
print('-------------')

# Calculate weight loss per month and display it in a table
for num in range(1, 7):
    weight -= 4
    print(num, '\t', weight)
    
