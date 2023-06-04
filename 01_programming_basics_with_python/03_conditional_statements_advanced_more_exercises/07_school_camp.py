season = input()
group = input()
students = int(input())
nights = int(input())
sport = ""
price = 0

if season == "Winter" and group == "girls":
    sport = "Gymnastics"
elif season == "Winter" and group == "boys":
    sport = "Judo"
elif season == "Winter" and group == "mixed":
    sport = "Ski"
elif season == "Spring" and group == "girls":
    sport = "Athletics"
elif season == "Spring" and group == "boys":
    sport = "Tennis"
elif season == "Spring" and group == "mixed":
    sport = "Cycling"
elif season == "Summer" and group == "girls":
    sport = "Volleyball"
elif season == "Summer" and group == "boys":
    sport = "Football"
elif season == "Summer" and group == "mixed":
    sport = "Swimming"

if season == "Winter":
    if group == "boys" or group == "girls":
        price = 9.6
    elif group == "mixed":
        price = 10
elif season == "Spring":
    if group == "boys" or group == "girls":
        price = 7.2
    elif group == "mixed":
        price = 9.5
elif season == "Summer":
    if group == "boys" or group == "girls":
        price = 15
    elif group == "mixed":
        price = 20

total_sum = students * price * nights

if students >= 50:
    total_sum *= 0.50
elif 20 <= students < 50:
    total_sum *= 0.85
elif 10 <= students < 20:
    total_sum *= 0.95

print(f"{sport} {total_sum:.2f} lv.")
