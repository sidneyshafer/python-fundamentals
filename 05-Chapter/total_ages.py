def main():
    # get user age
    first_age = int(input('Enter your age: '))
    second_age = int(input("Enter your dog's age: "))
    
    # define sum function
    def sum(num1, num2):
        return num1 + num2
    
    # get sum of both ages
    total = sum(first_age, second_age)

    # display the total age
    print('Together you are', total, 'years old.')

main()
