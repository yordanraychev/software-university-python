fuel_type = input()
litres = float(input())
card = input()
total_price = 0

if fuel_type == "Gasoline":
    if card == "Yes":
        gasoline_l = 2.22 - 0.18
        total_price = litres * gasoline_l
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90
    elif card == "No":
        total_price = litres * 2.22
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90

elif fuel_type == "Diesel":
    if card == "Yes":
        diesel_l = 2.33 - 0.12
        total_price = litres * diesel_l
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90
    elif card == "No":
        total_price = litres * 2.33
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90

elif fuel_type == "Gas":
    if card == "Yes":
        gas_l = 0.93 - 0.08
        total_price = litres * gas_l
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90
    elif card == "No":
        total_price = litres * 0.93
        if 20 < litres <= 25:
            total_price *= 0.92
        elif litres > 25:
            total_price *= 0.90

print(f"{total_price:.2f} lv.")
