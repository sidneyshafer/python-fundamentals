# This program demonstrates how to get the
# index of an item and replace it within a list

def main():
    # create a list
    food = ['Pizza', 'Burgers', 'Chips']

    # display the list
    print('Here are the items in the food list:')
    print(food)
    print()

    # get item to change
    item = input('Which item would you like to change? ')

    try:
        # get item's index
        item_index = food.index(item)

        # get the new item to replace it with
        new_item = input('Enter new item: ')

        # replace old item with new item
        food[item_index] = new_item

        # display new list
        print('Here is the new list:')
        print(food)
    except ValueError:
        print('Item was not found in list.')

main()
