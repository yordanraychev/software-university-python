budget = float(input())
season = input()
type_car = ""
class_type = ""
car_price = 0

if budget <= 100:
    class_type = "Economy class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.35
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.65
elif 100 < budget <= 500:
    class_type = "Compact class"
    if season == "Summer":
        type_car = "Cabrio"
        car_price = budget * 0.45
    elif season == "Winter":
        type_car = "Jeep"
        car_price = budget * 0.8
elif 500 < budget:
    class_type = "Luxury class"
    type_car = "Jeep"
    car_price = budget * 0.9

print(f"{class_type}")
print(f"{type_car} - {car_price:.2f}")
