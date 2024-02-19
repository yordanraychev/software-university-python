from collections import deque

money_in_pocket = [int(amount) for amount in input().split()]
foods_price = deque([int(price) for price in input().split()])
food_count = 0

while money_in_pocket and foods_price:
    current_amount = money_in_pocket[-1]
    current_food = foods_price[0]

    if current_food == current_amount or current_amount > current_food:
        food_count += 1
        if current_amount > current_food:
            if len(money_in_pocket) > 1:
                money_in_pocket[-2] += current_amount - current_food

    money_in_pocket.pop()
    foods_price.popleft()

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count == 0:
    print("Henry remained hungry. He will try next weekend again.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print(f"Henry ate: {food_count} foods.")
