# -------------------------------------
# This program defines the Driver class
# -------------------------------------

class Driver:
    # INITIALIZER METHOD
    def __init__(self, name, gender, hair, eyes, shirt, pants, shoes, age, birthday):
        self.__name = name
        self.__gender = gender
        self.__hair = hair
        self.__eyes = eyes
        self.__shirt = shirt
        self.__pants = pants
        self.__shoes = shoes
        self.__age = age
        self.__birthday = birthday

    # SETTER METHODS
    def set_name(self, name):
        self.__name = name
        
    def set_gender(self, gender):
        self.__gender = gender

    def set_hair(self, hair):
        self.__hair = hair

    def set_eyes(self, eyes):
        self.__eyes = eyes

    def set_shirt(self, shirt):
        self.__shirt = shirt

    def set_pants(self, pants):
        self.__pants = pants

    def set_shoes(self, shoes):
        self.__shoes = shoes

    def set_age(self, age):
        self.__age = age

    def set_birthday(self, birthday):
        self.__birthday = birthday

    # GETTER METHODS
    def get_name(self):
        return self.__name
    
    def get_gender(self):
        return self.__gender

    def get_hair(self):
        return self.__hair

    def get_eyes(self):
        return self.__eyes

    def get_shirt(self):
        return self.__shirt

    def get_pants(self):
        return self.__pants

    def get_shoes(self):
        return self.__shoes

    def get_age(self):
        return self.__age

    def get_birthday(self):
        return self.__birthday
