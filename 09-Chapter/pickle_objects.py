# This program demonstrates object pickeling
import pickle

def main():
    again = 'y'

    # Open a file for binary writing
    output_file = open('info.dat', 'wb')

    # Get data until the user wants to stop
    while again.lower() == 'y':
        save_data(output_file)

        again = input('Enter more data? (y/n): ')

    output_file.close()

def save_data(file):
    person = {}

    person['name'] = input('Name: ')
    person['age'] = int(input('Age: '))
    person['weight'] = float(input('Weight: '))

    # Pickle dictionary
    pickle.dump(person, file)

main()
