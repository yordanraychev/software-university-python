months = int(input())
electricity = 0
water = 0
internet = 0
other = 0

for m in range(months):
    electricity_per_month = float(input())
    water = months * 20
    internet = months * 15
    electricity = electricity + electricity_per_month
    other += (electricity_per_month + 20 + 15) + (electricity_per_month + 20 + 15) * 0.2

avg_sum = (electricity + water + internet + other) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {avg_sum:.2f} lv")
