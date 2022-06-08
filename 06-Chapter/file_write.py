# This program writes three lines of data to a file

def main():
    # open file
    outfile = open('philosophers.txt', 'w')

    # write to file
    outfile.write('John Locke\n')
    outfile.write('David Hume\n')
    outfile.write('Edmund Burke\n')

    # close file
    outfile.close()

# Call function
main()
