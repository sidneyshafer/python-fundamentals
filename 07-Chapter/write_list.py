# This program saves a list of strings to a file

def main():
    cities = ['New York', 'Boston', 'Atlanta', 'Dallas']

    outfile = open('cities.txt', 'w')

    for item in cities:
        outfile.write(item + '\n')

    outfile.close()

main()
