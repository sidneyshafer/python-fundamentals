# This program calculates the average of
# the values in a list

def main():
    scores = [2.5, 7.3, 6.5, 4.0, 5.2]

    total = 0.0

    for value in scores:
        total += value

    # calculate average
    average = total / len(scores)

    print('The average of the numbers is', average)

main()
