budget = float(input())
staff = int(input())
price_per_outfit = float(input())
decoration_price = budget * 0.10
outfits_price = staff * price_per_outfit

if staff > 150:
    outfits_price *= 0.9

needed_expenses = outfits_price + decoration_price
difference = abs(needed_expenses - budget)

if needed_expenses > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
