MIN_SALARY = 30000.0
MIN_YEARS = 2

# Get users annual salary
salary = float(input('Enter your annual salary: '))

# Get the number of years on current job
years_on_job = int(input('Enter the number of years employed: '))

# Determine whether the customer qualifies
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
else:
    print('You do not qualify for this loan')
