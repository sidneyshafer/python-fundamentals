# Define main function
def main():
    fat_grams = int(input('Enter the number of fat grams: '))
    carb_grams = int(input('Enter the nunmber of carb grams: '))
    fat_cal(fat_grams)
    carb_cal(carb_grams)

# Calculate the number of calories from fat
def fat_cal(num):
    fats = num * 9
    return fats

# Calculate the number of calories from carbs
def carb_cal(num):
    carbs = num * 4
    return carbs

main()
