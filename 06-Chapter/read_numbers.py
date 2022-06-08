# This program demonstrates how to read numbers
# from a file

def main():
    file = open('numbers.txt', 'r')

    # read three numbers from a file
    num1 = int(file.readline())
    num2 = int(file.readline())
    num3 = int(file.readline())

    # close the file
    file.close()

    # add the numbers
    total = num1 + num2 + num3

    # display numbers and their total
    print('The numbers are:', num1, num2, num3)
    print('Their total is:', total)

main()
