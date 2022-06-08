# ----------------------------------
# This program defines the Car class
# ----------------------------------

class Car:
    # INITILIZER METHOD
    def __init__(self, speed, distance):
        self.__speed = speed
        self.__distance = distance

    # SETTER METHODS
    def set_speed(self, speed):
        self.__speed = speed

    def set_distance(self, distance):
        self.__distance = distance

    # GETTER METHODS
    def get_speed(self):
        return self.__speed
    
    def get_distance(self):
        return self.__distance

    # GO METHOD
    def go(self):
        self.__distance /= self.__speed
