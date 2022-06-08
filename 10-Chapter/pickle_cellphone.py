# This program pickles CellPhone objects

import pickle
import cellphone

# Constant for filename
FILENAME = 'cellphones.dat'

def main():
    again = 'y'

    output_file = open(FILENAME, 'wb')

    while again.lower() == 'y':
        man = input('Enter the manufacturer: ')
        mod = input('Enter the model: ')
        retail = float(input('Enter the retail price: '))

        # Create CellPhone object
        phone = cellphone.CellPhone(man, mod, retail)

        # Pickle the object
        pickle.dump(phone, output_file)

        again = input('Enter more phone data? (y/n): ')

    # Close the file
    output_file.close()
    print('The data was written to', FILENAME)
        
main()
