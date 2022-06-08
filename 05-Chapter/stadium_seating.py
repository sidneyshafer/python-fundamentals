# This program displays the cost of seats sold in a stadium

def main():
    a = float(input('How many seats were sold in Class A? '))
    b = float(input('How many seats were sold in Class B? '))
    c = float(input('How many seats were sold in Class C? '))

    a_cost = a * 20.00
    b_cost = b * 15.00
    c_cost = c * 10.00

    total = a_cost + b_cost + c_cost

    print('The total income was ${t:,.2f}'.format(t=total))

main()
