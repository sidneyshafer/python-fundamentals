# This program reads a series of strings from 'names.txt'
# and displays the number of items in the file

def main():
    infile = open('names.txt', 'r')

    count = 0

    line = True
    
    while line != '':
        line = infile.readline()
        count += 1
        
    infile.close()

    print('The number of items in the text file is:', count)

main()
