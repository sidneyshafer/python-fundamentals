
def main():
    num = int(input('Enter a number: '))

    lines(num)

def lines(n):
    if n > 0:
        print('*')
        lines(n - 1)

main()
