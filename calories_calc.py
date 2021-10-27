quantityFoods = int(input('How many foods did you eat today? '))
food = ''
calories = 0

if quantityFoods > 0:
    for f in range(quantityFoods):
        food = (input('Food: '))
        calories += int(input('Calories: '))
    print(f'Total calories ingested today: {calories}')
else:
    print('No food eaten, total calories: 0')