# This program demonstrates the Car class

import vehicles

def main():
    # Create an object from the Car class
    used_car = vehicles.Car('Audi', 2007, 12500, 21500.0, 4)

    # Display the car's data
    print('Make:', used_car.get_make())
    print('Model:', used_car.get_model())
    print('Mileage:', used_car.get_mileage())
    print('Price:', used_car.get_price())
    print('Doors:', used_car.get_doors())

main()
