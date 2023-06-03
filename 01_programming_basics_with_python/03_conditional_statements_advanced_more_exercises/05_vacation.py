budget = float(input())
season = input()
location = ""
place_type = ""
price = 0

if budget <= 1000:
    place_type = "Camp"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.45
elif 1000 < budget <= 3000:
    place_type = "Hut"
    if season == "Summer":
        location = "Alaska"
        price = budget * 0.8
    elif season == "Winter":
        location = "Morocco"
        price = budget * 0.6
elif 3000 < budget:
    place_type = "Hotel"
    price = budget * 0.9
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {place_type} - {price:.2f}")
