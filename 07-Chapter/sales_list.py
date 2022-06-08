NUM_DAYS = 5

def main():
    # create a list
    sales = [0] * NUM_DAYS

    # create variable to hold an index
    index = 0

    print('Enter the sales for each day.')

    # get the sales for each day
    while index < NUM_DAYS:
        print('Day #', index + 1,': ', sep='', end='')
        sales[index] = float(input())
        index += 1

        # display the values entered
    print('Here are the values you entered:')
    for value in sales:
        print(value)

main()
