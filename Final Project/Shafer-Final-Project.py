   # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# || ------------------------------------------------------------- || #
# ||                                                               || #
# ||  This program displays information about a car's type and     || #
# ||  model year. It allows a user to look up, add, change,        || #
# ||  and delete the car type and model year. It also allows       || #
# ||  the user to create a driver and drive the car.               || #
# ||  When a user closes the program, the model year and type is   || #
# ||  pickeled into a file called 'cars.dat'.                      || #
# ||                                                               || #
# || ------------------------------------------------------------- || #
    # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

import pickle
import car
import driver

# ------------------
# CONSTANT VARIABLES
# ------------------
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
CREATE_DRIVER = 5
CALC_MPH = 6
QUIT = 7

FILENAME = 'cars.dat'

# -------------
# MAIN FUNCTION
# -------------
def main():

    cars = load_info()

    choice = 0

    while choice != QUIT:
        # Get user choice
        choice = menu_choice()

        if choice == LOOK_UP:
            look_up(cars)
        elif choice == ADD:
            add(cars)
        elif choice == CHANGE:
            change(cars)
        elif choice == CREATE_DRIVER:
            create_driver()
        elif choice == CALC_MPH:
            calc_mph()
        elif choice == DELETE:
            delete(cars)

    # When the file closes, save the
    # cars dictionary to 'cars.dat'
    save_data(cars)

# ------------------
# LOAD_INFO FUNCTION
# ------------------
def load_info():
    # Try loading the file information from 'cars.dat'
    try:
        input_file = open(FILENAME, 'rb')

        cars_dct = pickle.load(input_file)

        input_file.close()

    # If the file is empty, return an empty dictionary
    except IOError:
        cars_dct = {}

    # Return the cars dictionary
    return cars_dct


# --------------------
# MENU_CHOICE FUNCTION
# --------------------
def menu_choice():
    print()
    print()
    print('|---------------------------------|')
    print('|            MAIN MENU            |')
    print('|---------------------------------|')
    print('| 1. Look up a model year         |')
    print('| 2. Add a new car & model year   |')
    print('| 3. Change a model year          |')
    print('| 4. Delete a car & model year    |')
    print('| 5. Create a driver              |')
    print('| 6. Calculate drive time         |')
    print('| 7. Quit the program             |')
    print('|---------------------------------|')
    print()

    # Get the user's choice
    choice = int(input('Enter your choice: '))

    # Validate the choice
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # Return the choice
    return choice
    
# ----------------
# LOOK_UP FUNCTION
# ----------------
def look_up(cars):

    # Input a type of car
    car_type = input('Enter the type of car: ')

    # Print the model year associated
    # with the type of car
    print(cars[car_type])


# ------------
# ADD FUNCTION
# ------------
def add(cars):

    # Input the type of car
    # and model year
    car_type = input('Enter a type of car: ')
    year = input('Enter the model year: ')

    # Add the car type and model year
    # if it does not already exist
    if car_type not in cars:
        cars[car_type] = year
    else:
        print('That entry already exists.')

# ---------------
# CHANGE FUNCTION
# ---------------
def change(cars):

    # Input the car type
    car_type = input('Enter the type of car: ')

    # If ths car is in the dictionary,
    # input the new model year and
    # change the entry
    if car_type in cars:
        year = input('Enter a new model year: ')

        cars[car_type] = year
    else:
        print('The car is not found.')


# ---------------
# DELETE FUNCTION
# ---------------
def delete(cars):

    # Input the type of car to delete
    car_type = input('Enter a type of car: ')

    # If the car is in the dictionary,
    # delete the entry
    if car_type in cars:
        del cars[car_type]
    else:
        print('The car is not found.')

# ----------------------
# CREATE_DRIVER FUNCTION
# ----------------------
def create_driver():
    print()
    print('|---------------------------------|')
    print('| Answer The Following Questions: |')
    print('|---------------------------------|')

    # Get user input
    name = input("| Enter the driver's name: ")
    gender = input('| Male or female: ')
    hair = input('| Short or long hair: ')
    eyes = input('| Blue, brown, or green eyes: ')
    shirt = input('| Shirt color: ')
    pants = input('| Jeans, leggings, or shorts: ')
    shoes = input('| Crocs, sandles, or boots: ')
    age = int(input('| Enter the age: '))
    birthday = input('| Enter the birthday (mm/dd/yyyy): ')
    print('|--------------------------------------|')
    print()
    print()

    # Create an object from the Driver class
    my_driver = driver.Driver(name, gender, hair, eyes, shirt, pants, shoes, age, birthday)

    # Display the Driver information
    print('  *** YOUR DRIVER INFORMATION ***  ')    
    print('             --------              ')
    print('|---------------------------------|')
    print('|             DRIVER              |')
    print('|---------------------------------|')
    print('| Name:', my_driver.get_name())
    print('| Gender:', my_driver.get_gender())
    print('| Age:', my_driver.get_age())
    print('| Birthday:', my_driver.get_birthday())
    print('| Hair Style:', my_driver.get_hair())
    print('| Eye Color:', my_driver.get_eyes())
    print('| Shirt Color:', my_driver.get_shirt())
    print('| Pant Style:', my_driver.get_pants())
    print('| Shoe Type:', my_driver.get_shoes())
    print('|---------------------------------|')
    print()

# ------------------
# DRIVE_CAR FUNCTION
# ------------------
def calc_mph():

    # Input the speed
    speed = int(input('Enter the driving speed (MPH): '))
    # Input distance
    distance = int(input('How far do you want to go? '))

    # Create an object from the Car class
    my_car = car.Car(speed, distance)

    # Call the Car class go() method
    my_car.go()

    # Display the distance traveled
    print()
    print('|--------------------------------|')
    print('| The speed is', speed, 'MPH')
    print('| THE CAR IS DRIVING...')
    print('| Your trip took', format(my_car.get_distance(), '.2f'), 'hours')
    print('|--------------------------------|')

# ------------------
# SAVE_DATA FUNCTION
# ------------------
def save_data(login_info):

    # Open the 'cars.dat' file
    output_file = open(FILENAME, 'wb')

    # Pickle the information from the dictionary
    pickle.dump(login_info, output_file)

    # Close the file
    output_file.close()

# Call the main function
main()
