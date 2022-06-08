# This program demonstrates how to write numbers
# to a text file

def main():
    file = open('numbers.txt', 'w')

    # get three numbers from user
    num1 = int(input('Enter a number: '))
    num2 = int(input('Enter another number: '))
    num3 = int(input('Enter one more number: '))

    # write the numbers to the file
    file.write(str(num1) + '\n')
    file.write(str(num2) + '\n')
    file.write(str(num3) + '\n')

    # close the file
    file.close()
    print('Data written to numbers.txt')

main()
