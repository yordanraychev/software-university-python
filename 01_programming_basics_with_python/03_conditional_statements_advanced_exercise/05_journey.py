budget = float(input())
season = input()
location = ""
accommodation = ""
expenses = 0

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        expenses = budget * 0.3
    elif season == "winter":
        expenses = budget * 0.7
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        expenses = budget * 0.4
    elif season == "winter":
        expenses = budget * 0.8
else:
    location = "Europe"
    expenses = budget * 0.9

if season == "summer" and location != "Europe":
    accommodation = "Camp"
else:
    accommodation = "Hotel"

print(f"Somewhere in {location}")
print(f"{accommodation} - {expenses:.2f}")
