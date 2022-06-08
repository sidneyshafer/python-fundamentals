# This program tests the CellPhone class

import cellphone

def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    # Create an instance of the CellPhone class
    phone = cellphone.CellPhone(man, mod, retail)

    # Display the data that was entered
    print()
    print('Here is the data you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('Model:', phone.get_model())
    print('Retail Price: $', format(phone.get_retail_price(), ',.2f'), sep='')

main()
