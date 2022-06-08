# if statement test_average

HIGH_SCORE = 95

# get three test scores
test1 = int(input('Enter test score 1: '))
test2 = int(input('Enter test score 2: '))
test3 = int(input('Enter test score 3: '))

# calculate average test score
average = (test1 + test2 + test3) / 3

# print average
print('The average score is ', average)

# If the average is a high score, congratulate the user.
if average >= HIGH_SCORE:
    print('Congrats!')
    print('You have a a high score!')
