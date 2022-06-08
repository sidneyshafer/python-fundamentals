# This program displays the number of calories from fat grams and carb grams

def main():
    fat_grams = int(input('Enter the number of fat grams: '))
    carb_grams = int(input('Enter the number of carb grams: '))
    fat_calories = fat_grams * 9
    carb_calories = carb_grams * 4
    total_calories = fat_calories + carb_calories
    print('Fat calories = {f:.2f}'.format(f=fat_calories))
    print('Carb calories = {c:.2f}'.format(c=carb_calories))
    print('Total calories = {t:.2f}'.format(t=total_calories))

main()

# This program calculates the calories without printing them

def calorie_calc():
    fat_grams = int(input('Enter the number of fat grams: '))
    carb_grams = int(input('Enter the number of carb grams: '))
    fat_calories = fat_grams * 9
    carb_calories = carb_grams * 4
    total_calories = fat_calories + carb_calories
    return total_calories
