width_meters = float(input())
height_meters = float(input())

height_cm = height_meters * 100
width_cm = width_meters * 100

height_minus_aisle = height_cm - 100
desks = height_minus_aisle // 70
rows = width_cm // 120
seats_count = rows * desks - 3

print(f"{seats_count:.0f}")
