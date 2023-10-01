money = input().split(", ")
beggars = int(input())
money_as_digits = []
for digit in money:
    money_as_digits.append(int(digit))
sums_beggars = []
initial_index = 0
while initial_index < beggars:
    current_beggar_sum = 0
    for current_index in range(initial_index, len(money_as_digits), beggars):
        current_beggar_sum += money_as_digits[current_index]
    sums_beggars.append(current_beggar_sum)
    initial_index += 1
print(sums_beggars)
