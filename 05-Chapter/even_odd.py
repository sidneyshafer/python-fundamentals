# define function using boolean values
def is_even(number):
    # determine if number is even
    if (number % 2) == 0: # % operator returns remainder
        status = True
    else:
        status = False

    return status

number = int(input('Enter a number: '))
if is_even(number):
    print('The number is even.')
else:
    print('The number is odd.')
