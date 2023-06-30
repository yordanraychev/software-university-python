coins_1 = int(input())
coins_2 = int(input())
banknotes_5 = int(input())
total_sum = int(input())

for a in range(coins_1 + 1):
    for b in range(coins_2 + 1):
        for c in range(banknotes_5 + 1):
            if total_sum == a + b * 2 + c * 5:
                print(f"{a} * 1 lv. + {b} * 2 lv. + {c} * 5 lv. = {total_sum} lv.")
