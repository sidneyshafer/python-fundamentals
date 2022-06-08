# This program reads a series of integers in the numbers2.txt file

def main():
    number_file = open('numbers2.txt', 'r')

    number = number_file.readlines()

    for num in number:
        num.strip('\n')
        print(num)

    number_file.close()
    
main()
