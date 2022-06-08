DAYS = 5 # maxium number of days
total_bugs = 0 # accumulator

# explain the program
print('This program calculates the total')
print('number of bugs collected over', DAYS, 'days.')

# get numbers a accumulate
for x in range(DAYS):
    bugs = int(input('Enter the number of bugs: '))
    total_bugs = total_bugs + bugs

# display total nummber of bugs
print('The total number of bugs collected is', total_bugs)
