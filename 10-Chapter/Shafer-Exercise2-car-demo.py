# ---------------------------------------
# This program demonstrates the Car class
# ---------------------------------------

import car

def main():
    year = input("Enter the car's model year: ")
    make = input("Enter the car's make model: ")
    
    my_car = car.Car(year, make)

    print()
    print("The speed is zero...")
    print("I am going to accelerate five times...")
    print("Here are the speeds at each instance:")
    for count in range(5):
        my_car.accelerate()
        print(my_car.get_speed())

    print()
    print("Now I am going to brake five times!")
    print("Here are the new speeds at each instance:")
    for count in range(5):
        my_car.brake()
        print(my_car.get_speed())

main()
