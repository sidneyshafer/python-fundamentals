# get price of each item
item1 = float(input('What is the price of your first item? '))
item2 = float(input('What is the price of your second item? '))
item3 = float(input('What is the price of your third item? '))
item4 = float(input('What is the price of your fourth item? '))
item5 = float(input('What is the price of your fifth item? '))

# assign the sales tax
tax = 0.07

# calculate the subtotal
subtotal = item1 + item2 + item3 + item4 + item5

# calculate the amount of sales tax
sales_tax = subtotal * tax

# calculate total
total = subtotal + sales_tax

# print subtotal, sales tax, and total
print('Subtotal: ', subtotal)
print('Sales Tax: ', sales_tax)
print('Total: ', total)
