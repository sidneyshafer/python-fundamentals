# This program imports the Information module
# and creates three instances of the Information class

import info

def main():
    people = make_list()

    print('Here is the data you entered:')
    display_list(people)

def make_list():
    person_list = []

    print('Enter data for three people.')
    for count in range(1,4):
        print('Person #' + str(count) + ':')
        name = input('Enter name: ')
        address = input('Enter address: ')
        age = int(input('Enter age: '))
        phone = input('Enter phone number: ')
        print()

        person = info.Information(name, address, age, phone)

        person_list.append(person)

    return person_list

def display_list(person_list):
    for item in person_list:
        print(item.get_name())
        print(item.get_address())
        print(item.get_age())
        print(item.get_phone())
        print()

main()
