# This program gets the intials ofa user's
# first, middle, and last name

def main():
    name = input('Enter your full name: ')
    name_list = name.split()

    print(name_list[0][0], name_list[1][0], name_list[2][0])

main()
