# This program uses a function to create a list
# The function returns a reference to the list

def main():
    numbers = get_values()
    print('The numbers in the list are:')
    print(numbers)

def get_values():
    values = []

    again = 'y'

    while again == 'y':
        num = int(input('Enter a number: '))
        values.append(num)
        print()

        print('Add another number?')
        again = input('y = yes, n = no: ')
        print()

    return values

main()
