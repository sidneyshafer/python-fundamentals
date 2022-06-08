# This program displays the sum of
# digits in a string

def main():
    numbers = input('Enter a series of digits: ')

    total = 0

    for char in numbers:
        total += int(char)

    print(total)

main()
