# This program demonstrates the append method

def main():
    # create an empty list
    name_list = []

    # create a variable to control the loop
    again = 'y'

    # add names to the list
    while again == 'y':
        name = input('Enter a name: ')
        name_list.append(name)

        print('Do you want to add another name?')
        again = input('y = yes, n = no: ')
        print()

    # display names
    print('Here are the names you entered: ')

    for name in name_list:
        print(name)

main()
    
