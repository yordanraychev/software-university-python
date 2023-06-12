pairs = int(input())
previous_pair_sum = 0
total_sum = 0
max_diff = 0

for num in range(pairs):
    number1 = int(input())
    number2 = int(input())
    pair_sum = number1 + number2
    total_sum = total_sum + pair_sum
    if total_sum != pair_sum * pairs:
        max_diff = abs(previous_pair_sum - pair_sum)
        previous_pair_sum = pair_sum

if total_sum == pair_sum * pairs:
    print(f"Yes, value={pair_sum:.0f}")
elif total_sum != pair_sum * pairs:
    print(f"No, maxdiff={max_diff:.0f}")
