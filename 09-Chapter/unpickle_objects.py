# This program demonstrates unpickling.
import pickle

def main():
    end_of_file = False # To indicate end of file

    # Open file for binary reading
    input_file = open('info.dat', 'rb')

    # Read the end of the file
    while not end_of_file:
        try:
            # Unpickle the next object
            person = pickle.load(input_file)
            # Display the object
            display_data(person)
        except EOFError:
            end_of_file = True

    input_file.close()

def display_data(person):
    print('Name:', person['name'])
    print('Age:', person['age'])
    print('Weight:', person['weight'])
    print()

main()
