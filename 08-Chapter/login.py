
def main():
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')

    login_name = get_login_name(first, last, idnumber)

    print('Your system login name is: {}'.format(login_name))


def get_login_name(first, last, idnumber):
    set1 = first[0:3] # get first 3 digits
    set2 = last[0:3] # get first 3 digits
    set3 = idnumber[-3:] # get last 3 digits

    login_name = set1 + set2 + set3

    return login_name

main()
