# This program writes a series of numbers to a file

def main():
    outfile = open('numbers2.txt', 'w')

    numbers = int(input('How many numbers do you want to write? '))

    for num in range(1, numbers + 1):
        outfile.write(str(num) + '\n')

    # close file
    outfile.close()
    print('Numbers written to numbers2.txt')

main()
