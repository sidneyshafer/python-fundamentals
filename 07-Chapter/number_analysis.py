# This program asks the user for 20 numbers
# and stores them in a list

NUM = 5

def main():
    numbers = get_values()

    total = 0
    for value in numbers:
        total += value

    average = total / len(numbers)

    print('Lowest Number:', min(numbers))
    print('Highest Number:', max(numbers))
    print('Total:', total)
    print('Average:', average)

def get_values():
    values = [0] * NUM

    print('Enter a series of numbers:')

    index = 0
    while index < NUM:
        print('Number ', index + 1,': ', sep='', end='')
        values[index] = int(input())
        index += 1

    return values
    
main()
