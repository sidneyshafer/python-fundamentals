# Demonstrates a math function
import math

def main():
    number = float(input('Enter a number: '))
    square_root = math.sqrt(number)
    print('The square root of {n:.1f} is {s:.1f}'.format(n=number,s=square_root))

main()
