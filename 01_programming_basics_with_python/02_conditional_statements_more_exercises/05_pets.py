from math import floor, ceil

days = int(input())
food_given = int(input())
dog_food_daily = float(input())
cat_food_daily = float(input())
turtle_food_daily = float(input())
dog_food = dog_food_daily * days
cat_food = cat_food_daily * days
turtle_food = turtle_food_daily * days / 1000
food_eaten = dog_food + cat_food + turtle_food
difference = abs(food_given - food_eaten)

if food_given >= food_eaten:
    print(f"{floor(difference)} kilos of food left.")
else:
    print(f"{ceil(difference)} more kilos of food are needed.")
