# Define main function

def main():
    purchase_amt = float(input('How much did your purchase cost? '))

    state_tax = get_state_tax(purchase_amt)
    county_tax = get_county_tax(purchase_amt)
    total_tax = county_tax + state_tax
    total_sales = purchase_amt + total_tax
    
    print('Purchase Amount: ${0:.2f}'.format(purchase_amt))
    print('State Tax: ${0:.2f}'.format(state_tax))
    print('County Tax: ${0:.2f}'.format(county_tax))
    print('Total Tax: ${0:.2f}'.format(total_tax))
    print('Total Sale: ${0:.2f}'.format(total_sales))

# Calculate state tax 
def get_state_tax(value):
    state_tax = value * 0.05
    return state_tax

# Calculate county tax 
def get_county_tax(value):
    county_tax = value * 0.025
    return county_tax


main()
