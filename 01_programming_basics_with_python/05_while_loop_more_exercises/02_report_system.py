expected_sum = int(input())
count = 0
count_cash = 0
count_card = 0
sum_cash = 0
sum_card = 0
total_sum = 0
collected = False
price = input()

while price != "End":
    price = int(price)
    count += 1

    if count % 2 == 0:
        if price >= 10:
            count_card += 1
            sum_card += price
            total_sum += sum_card
            print("Product sold!")
        else:
            print("Error in transaction!")

    if count % 2 != 0:
        if price <= 100:
            count_cash += 1
            sum_cash += price
            total_sum += sum_cash
            print("Product sold!")
        else:
            print("Error in transaction!")

    if total_sum >= expected_sum:
        collected = True
        break

    price = int(input())

if collected:
    avg_cash = sum_cash / count_cash
    avg_card = sum_card / count_card
    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
else:
    print("Failed to collect required money for charity.")
