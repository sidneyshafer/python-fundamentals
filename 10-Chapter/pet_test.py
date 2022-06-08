# This program tests the Pet class

import pet

def main():
    name = input("Enter your pet's name: ")
    animal = input("What type of animal is your pet? ")
    age = int(input("Enter your pet's age: "))

    mypet = pet.Pet(name, animal, age)

    print()
    print("Here is the data you entered:")
    print("Name:", mypet.get_name())
    print("Animal:", mypet.get_animal_type())
    print("Age:", mypet.get_age())

main()
