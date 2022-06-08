CONTRIB_RATE = 0.05

def main():
    gross_pay = float(input('Enter the gross pay: '))
    bonus = float(input('Enter the amount of bonuses: '))
    show_pay(gross_pay)
    show_bonus(bonus)

def show_pay(gross):
    contrib = gross * CONTRIB_RATE
    print('Contribution for gross pay: $',
          format(contrib, ',.2f'),
          sep='')

def show_bonus(bonus):
    contrib = bonus * CONTRIB_RATE
    print('Contribution for bonuses: $',
          format(contrib, ',.2f'),
          sep='')

# Call function
main()
