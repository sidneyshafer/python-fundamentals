# This program reads numbers from a file into a list
# and checks to see if a user-entered number is in the list

def main():
    infile = open('charge_accounts.txt', 'r')

    numbers = infile.readlines()

    infile.close()

    num = int(input('Enter a seven-digit charge account number: '))

    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    if num in numbers:
        print('The number is valid')
    else:
        print('The number is invalid')

main()
