# This program manages contacts
import contact
import pickle

# GLOBAL CONSTANTS
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'contacts.dat'


# MAIN FUNCTION
def main():
    # Load existing dictionary and
    # assign it to mycontacts
    mycontacts = load_contacts()

    choice = 0

    while choice != QUIT:
        choice = get_menu_choice()

        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)

    # Save the mycontacts dictionary
    # to a file
    save_contacts(mycontacts)


# LOAD FUNCTION
def load_contacts():
    try:
        input_file = open(FILENAME, 'rb')

        contact_dct = pickle.load(input_file)

        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary
        contact_dct = {}

    return contact_dct


# MENU CHOICE FUNCTION
def get_menu_choice():
    print()
    print('Menu')
    print('-------------------------------')
    print('1. Look up a contact')
    print('2. Add a new contact')
    print('3. Change an existing contact')
    print('4. Delete a contact')
    print('5. Quit the program')
    print()

    choice = int(input('Enter your choice: '))

    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice


# LOOK_UP FUNCTION
def look_up(mycontacts):
    name = input('Enter a name: ')

    print(mycontacts.get(name, 'That name is not found'))


# ADD FUNCTION
def add(mycontacts):
    name = input('Name: ')
    phone = input('Phone: ')
    email = input('Email: ')

    entry = contact.Contact(name, phone, email)

    if name not in mycontacts:
        mycontacts[name] = entry
        print('The entry has been added')
    else:
        print('That name already exists.')


# CHANGE FUNCTION
def change(mycontacts):
    name = input('Enter a name: ')

    if name in mycontacts:
        phone = input('Enter a new phone number: ')
        email = input('Enter a new email address: ')

        # Create an object
        entry = contact.Contact(name, phone, email)

        # Update the entry
        mycontacts[name] = entry
        print('Information updated.')
    else:
        print('Name not found.')


# DELETE FUNCTION
def delete(mycontacts):
    name = input('Enter a name: ')

    if name in mycontacts:
        del mycontacts[name]
        print('Entry deleted.')
    else:
        print('Name not found.')


# SAVE_CONTACTS FUNCTION
def save_contacts(mycontacts):
    output_file = open(FILENAME, 'wb')

    pickle.dump(mycontacts, output_file)

    output_file.close()

main()
