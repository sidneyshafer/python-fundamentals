# ----------------------------------
# This program creates a Car, Truck,
# and SUV object
# ----------------------------------

import vehicles

def main():
    # Create a Car object
    car = vehicles.Car('BMW', 2001, 70000, 15000.0, 4)

    # Create a Truck object
    truck = vehicles.Truck('Toyota', 2002, 40000, 12000.0, '4WD')

    # Create a SUV object
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500.0, 5)

    print('USED CAR INVENTORY')
    print('==================')

    # Display the car's data
    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Doors:', car.get_doors())
    print()

    # Display the truck's data
    print('The following pickup truck is in inventory:')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive Type:', truck.get_drive_type())
    print()

    # Display the SUV's data
    print('The following SUV is in inventory:')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())
    print()

main()
