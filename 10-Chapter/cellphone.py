# The CellPhone class holds data about a cell phone

class CellPhone:

    # The __init__ method initializes the attributes

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # MUTATOR METHODS

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_retail_price(self, price):
        self.__retail_price = price

    # ACCESSOR METHODS

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
