# This program uses try/except statements
# to calculate gross pay

def main():
    try:
        hours = int(input('How many hours did you work? '))
        pay_rate = float(input('Enter hourly pay rate: '))

        gross_pay = hours * pay_rate

        print('Gross Pay: ${0:,.2f}'.format(gross_pay))
    except ValueError as err:
        print(err)
    except:
        print('An error occured.')

main()
