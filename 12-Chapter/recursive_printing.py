# ----------------------------------------
# This program displays recursive printing
# ----------------------------------------

def main():
    num = int(input('Enter a number: '))

    message(num)

def message(n):
    if n > 0:
        print(n)
        message(n - 1)

main()
