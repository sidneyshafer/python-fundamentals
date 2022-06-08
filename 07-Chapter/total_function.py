# This program uses a function to calculate the
# total of the values in a list

def main():
    numbers = [2,4,6,8,10]

    print('The total is', get_total(numbers))

# define get_total function
def get_total(value_list):
    total = 0

    for value in value_list:
        total += value

    return total

main()
