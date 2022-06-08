# This program reads a series of integers from 'numbers.txt'
# and calculates their total

def main():
    infile = open('numbers.txt', 'r')

    total = 0

    for line in infile:
        num = int(line)
        total += num

    infile.close()

    print('The total is:', total)

main()
