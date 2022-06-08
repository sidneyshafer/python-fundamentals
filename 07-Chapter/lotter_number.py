# This program generates a list of seven lottery numbers
# and stores them in a list

import random

def main():
    lottery_list = get_values()
    print('The Lottery Numbers Are:')
    for num in lottery_list:
        print(num)

def get_values():
    numbers = []

    index = 0
    while index < 7:
        num = random.randint(0,9)
        numbers.append(num)
        index += 1
    return numbers

main()
        
