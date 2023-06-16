balance = 0

while True:
    amount = input()

    if amount == "NoMoreMoney":
        break

    current_sum = float(amount)

    if current_sum >= 0:
        balance += current_sum
        print(f"Increase: {current_sum:.2f}")
    else:
        print("Invalid operation!")
        break

print(f"Total: {balance:.2f}")
