inherited_money = float(input())
year = int(input())

age = 17
spendings = inherited_money

for y in range(1800, year + 1):
    if y % 2 == 0:
        spendings = spendings - 12000
    else:
        age = age + 2
        spendings = spendings - (12000 + 50 * age)

if spendings >= 0:
    print(f"Yes! He will live a carefree life and will have {spendings:.2f} dollars left.")
else:
    print(f"He will need {abs(spendings):.2f} dollars to survive.")
