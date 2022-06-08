# Calculates the length of a right triangle's hypotenuse

import math

def main():
    a = float(input('Enter the length of side A: '))
    b = float(input('Enter the length of side B: '))

    c = math.hypot(a,b)

    print('The length of the hypotenuse is {c:.2f}'.format(c=c))

main()
