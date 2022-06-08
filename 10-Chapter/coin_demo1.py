import random

class Coin:

    def __init__(self):
        # __ TWO UNDERSCORES HIDES THE ATTRIBUTE
        self.__sideup = 'Heads'

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup

def main():
    my_coin = Coin()
    print('This side is up:', my_coin.get_sideup())

    print('I am tossing the coin...')
    my_coin.toss()

    print('This side is up:', my_coin.get_sideup())
    print()

    print('I am going to toss the coin ten times:')
    for count in range(10):
        my_coin.toss()
        print(my_coin.get_sideup())

main()
