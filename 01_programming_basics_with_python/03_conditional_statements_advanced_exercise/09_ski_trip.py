days = int(input())
room_type = input()
feedback = input()

nights = days - 1
price_per_night = 0

if room_type == "room for one person":
    price_per_night = 18
elif room_type == "apartment":
    price_per_night = 25
    if nights < 10:
        price_per_night *= 0.7
    elif nights <= 15:
        price_per_night *= 0.65
    elif nights > 15:
        price_per_night *= 0.5
elif room_type == "president apartment":
    price_per_night = 35
    if nights < 10:
        price_per_night *= 0.9
    elif nights <= 15:
        price_per_night *= 0.85
    elif nights > 15:
        price_per_night *= 0.8

total_sum = nights * price_per_night

if feedback == "positive":
    total_sum *= 1.25
elif feedback == "negative":
    total_sum *= 0.9

print(f"{total_sum:.02f}")
