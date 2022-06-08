# This program assigns random numbers to
# a two-dimensional list

import random

ROWS = 3
COLS = 4

def main():
    values = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    for r in range(ROWS):
        for c in range(COLS):
            values[r][c] = random.randint(1,50)

    print(values)

main()
