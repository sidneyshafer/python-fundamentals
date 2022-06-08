# Get width and length of rectangles

r1_width = int(input('What is the width of the first rectangle? '))
r1_length = int(input('What is the length of the first rectangle? '))
r2_width = int(input('What is the width of the second rectangle? '))
r2_length = int(input('What is the length of the second rectangle? '))

r1 = r1_width * r1_length
r2 = r2_width * r2_length

if r1 > r2:
    print('The first rectangle is bigger.')
elif r1 < r2:
    print('The second rectangle is bigger.')
else:
    print('The rectangles are equal.')
