# This program calculates an item's sale price

DISCOUNT = 0.20

# Get regular price function
def get_reg_price():
    price = float(input("Enter the item's price: "))
    return price

# Get discount price function
def discount(price):
    return price * DISCOUNT

# Main function
def main():
    reg_price = get_reg_price
    sale_price = reg_price - discount(reg_price)
    print('The sale price is $ {sp.2f}'.format(sp=sale_price))
    
main()
