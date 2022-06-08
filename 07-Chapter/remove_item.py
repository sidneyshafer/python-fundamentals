# This program demonstrates how to remove an item
# from a list

def main():
    # create a list
    food = ['Pizza', 'Burgers', 'Chips', 'Fries']

    # display the list
    print('Here are the list items:')
    print(food)
    print()

    # get item to change
    item = input('Which item should I remove? ')
    print()

    try:
        food.remove(item)
        print('Here is the new list:')
        print(food)
    except ValueError:
        print('The item was not found in the list.')

main()
