# This program asks a user to enter the sales for each
# day of the week and calculates their total

NUM_DAYS = 7

def main():
    # create a list
    sales = [0] * NUM_DAYS

    index = 0

    total = 0.0

    print('Enter the sales for each day.')

    # get the sales for each day
    while index < NUM_DAYS:
        print('Day #', index + 1,': ', sep='', end='')
        sales[index] = float(input())
        index += 1

    for value in sales:
        total += value

    print('Total Sales: $', total, sep='')

main()
