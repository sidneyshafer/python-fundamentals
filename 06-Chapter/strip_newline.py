# This program reads the contents of the philosophers.txt file

def main():
    infile = open('philosophers.txt', 'r')

    # read each line from file
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # strip the /n from each line
    line1 = line1.strip()
    line2 = line2.strip()
    line3 = line3.strip()

    # close the file
    infile.close()

    # print the data
    print(line1)
    print(line2)
    print(line3)

main()
