
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'info.dat'

def main():

    login_info = load_info()

    choice = 0

    while choice != QUIT:

        choice = menu_choice()

        if choice == LOOK_UP:
            look_up(login_info)
        elif choice == ADD:
            add(login_info)
        elif choice == CHANGE:
            change(login_info)
        elif choice == DELETE:
            delete(login_info)

    save_data(login_info)


# LOAD_INFO FUNCTION
def load_info():
    try:
        input_file = open(FILENAME, 'rb')

        info_dct = pickle.load(input_file)

        input_file.close()
    except IOError:
        info_dct = {}

    return info_dct


# MENU_CHOICE FUNCTION
def menu_choice():
    print()
    print('Login Information')
    print('-------------------------')
    print('1. Look up an email address')
    print('2. Add a new name & email address')
    print('3. Change an email address')
    print('4. Delete a name & email address')
    print('5. Quit the program & save to a file')
    print()

    # Get the user's choice
    choice = int(input('Enter your choice: '))

    # validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    return choice
    

# LOOK_UP FUNCTION
def look_up(login_info):
    name = input('Enter a name: ')

    print(login_info[name])


# ADD FUNCTION
def add(login_info):
    name = input('Enter a name: ')
    email = input('Enter an email: ')

    if name not in login_info:
        login_info[name] = email
    else:
        print('That entry already exists.')


# CHANGE FUNCTION
def change(login_info):
    name = input('Enter a name: ')

    if name in login_info:
        email = input('Enter a new email: ')

        login_info[name] = email
    else:
        print('The name is not found.')


# DELETE FUNCTION
def delete(login_info):
    name = input('Enter a name: ')

    if name in login_info:
        del login_info[name]
    else:
        print('That name is not found.')


# SAVE_DATA FUNCTION
def save_data(login_info):
    output_file = open(FILENAME, 'wb')

    pickle.dump(login_info, output_file)

    output_file.close()

main()
