number_of_orders = int(input())
total_sum = 0
for _ in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed = int(input())
    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed <= 2000 and number_of_orders > 0:
        total_price = price_per_capsule * days * capsules_needed
        print(f"The price for the coffee is: ${total_price:.2f}")
        total_sum += total_price
    else:
        continue
print(f"Total: ${total_sum:.2f}")
