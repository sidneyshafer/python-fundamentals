# This program displays the rolling of dice

import random

MIN = 1
MAX = 6

def main():
    # variable to control loop
    again = 'y'

    while again == 'y' or again == 'Y':
        print('Rolling the dice...')
        print('Their values are:',
              random.randint(MIN, MAX),
              'and',
              random.randint(MIN, MAX),
              sep=' ')

        again = input('Roll again? (y = yes): ')

# Call main function
main()
