# This program passes a Coin object as
# an argument

import coin

def main():
    my_coin = coin.Coin()

    print(my_coin.get_sideup())

    # Pass object to flip function
    flip(my_coin)

    # Display the new sideup
    print(my_coin.get_sideup())

def flip(coin_obj):
    coin_obj.toss()

main()
