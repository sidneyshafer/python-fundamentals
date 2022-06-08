# ----------------------------------------
# This program uses recursion to calculate
# the factorial of a number
# ----------------------------------------

def main():
    number = int(input('Enter a non-negative integer: '))

    fact = factorial(number)

    print('The factorial of', number, 'is', fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

main()
