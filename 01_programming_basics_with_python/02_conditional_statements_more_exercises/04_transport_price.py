distance_km = int(input())
travel_type = input()
taxi_initial_fee = 0.70
taxi_fee = 0
travel_price = 0

if travel_type == "day":
    taxi_fee = 0.79
elif travel_type == "night":
    taxi_fee = 0.90

if distance_km < 20:
    travel_price = distance_km * taxi_fee + taxi_initial_fee
    print(f"{travel_price:.2f}")
elif distance_km >= 100:
    travel_price = distance_km * 0.06
    print(f"{travel_price:.2f}")
else:
    travel_price = distance_km * 0.09
    print(f"{travel_price:.2f}")
