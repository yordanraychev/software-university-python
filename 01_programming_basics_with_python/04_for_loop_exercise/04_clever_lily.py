age = int(input())
laundry = float(input())
price_per_toy = int(input())
toys = 0
total_sum = 0
current_money = 0
for bday in range(1, age + 1):
    if bday % 2 == 0:
        current_money += 10
        total_sum += current_money - 1
    else:
        toys += 1
total_sum += toys * price_per_toy
diff = abs(total_sum - laundry)
if total_sum >= laundry:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}" )
