season = input()
kms = float(input())
price = 0

if kms <= 5000:
    if season == "Spring" or season == "Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.9
    elif season == "Winter":
        price = 1.05
elif 5000 < kms <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.1
    elif season == "Winter":
        price = 1.25
elif 10000 < kms <= 20000:
    price = 1.45

salary_per_season = price * kms * 4
salary_net = salary_per_season * 0.9

print(f"{salary_net:.2f}")
