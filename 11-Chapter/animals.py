# --------------------------------------------
# The Mammal class represents a generic mammal
# --------------------------------------------

class Mammal:

    def __init__(self, species):
        self.__species = species

    def show_species(self):
        print('I am a', self.__species)

    def make_sound(self):
        print('Grrrr')

# -----------------------------------------------
# The Dog class is a subclass of the mammal class
# -----------------------------------------------

class Dog(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Dog')

    def make_sound(self):
        print('Whoof! Whoof!')

# -----------------------------------------------
# The Cat class is a subclass of the mammal class
# -----------------------------------------------

class Cat(Mammal):

    def __init__(self):
        Mammal.__init__(self, 'Cat')

    def make_sound(self):
        print('Meow')
