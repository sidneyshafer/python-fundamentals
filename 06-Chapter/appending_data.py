# This program opens the philosophers.txt file
# and appends data

def main():
    infile = open('philosophers.txt', 'a')

    # append data
    infile.write('Sidney Shafer\n')
    infile.write('Allie Shafer\n')
    infile.write('Brent Shafer\n')
    infile.write('Lisa Shafer\n')

    # close file
    infile.close()

main()
