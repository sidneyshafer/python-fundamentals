# This program asks a user for the name of a file
# and prints out the contents

def main():
    file = input('Enter file name (end with .txt): ')
    infile = open(file, 'r')

    # read first five lines of file

    for line in range(0,6):
        line = infile.readline()
        line = line.strip('\n')
        print(line)

    # close file
    infile.close()

main()
