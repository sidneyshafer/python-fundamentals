# This program reads numbers from a file into a list

def main():
    infile = open('numbers.txt', 'r')

    numbers = infile.readlines()

    infile.close()

    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    print(numbers)

main()
