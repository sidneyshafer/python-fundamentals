# This program calls the split method,
# using the '/' as a seperator

def main():
    date = '03/30/2004'
    date_list = date.split('/')

    print(date_list)
    print('Month:', date_list[0])
    print('Day:', date_list[1])
    print('Year:', date_list[2])

main()
