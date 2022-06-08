# This program converts kilometers to miles

def main():
    kilometers = float(input('Enter a distance in kilometers: '))
    miles = kilometers * 0.6214
    print('{k:.2f} kilometers is {m:.2f} miles'.format(k=kilometers,m=miles))

main()
