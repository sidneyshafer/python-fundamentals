# This program reads the date from a user
# and converts it to a different format

def main():
    date_string = input('Enter a date (mm/dd/yyyy): ')

    date_list = date_string.split('/')

    if date_list[0] == '01':
        print('January ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '02':
        print('February ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '03':
        print('March ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '04':
        print('April ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '05':
        print('May ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '06':
        print('June ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '07':
        print('July ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '08':
        print('August ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '09':
        print('September ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '10':
        print('October ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '11':
        print('November ' + date_list[1]+', ' + date_list[2])
    elif date_list[0] == '12':
        print('December ' + date_list[1]+', ' + date_list[2])

main()
