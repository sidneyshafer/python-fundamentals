# This program demonstrates the in operator

def main():
    # create a list of names
    shafer_names = ['Brent', 'Sidney', 'Allie', 'Lisa']

    # Get name for search
    search = input('Enter a Shafer name: ')

    # determine whether the name is in the list
    if search in shafer_names:
        print(search, 'was found in the list.')
    else:
        print(search, 'was not found in the list.')

main()
