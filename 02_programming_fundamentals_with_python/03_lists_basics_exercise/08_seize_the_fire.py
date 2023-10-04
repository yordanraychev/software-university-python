fires_with_their_cells = input().split("#")
water = int(input())
effort, total_fire = 0, 0
cells = []
for fire in fires_with_their_cells:
    fire_level, water_needed = fire.split(" = ")
    needed_water = int(water_needed)
    is_valid = False
    if fire_level == "High" and 81 <= needed_water <= 125 and (water - needed_water) >= 0:
        is_valid = True
    elif fire_level == "Medium" and 51 <= needed_water <= 80 and (water - needed_water) >= 0:
        is_valid = True
    elif fire_level == "Low" and 1 <= needed_water <= 50 and (water - needed_water) >= 0:
        is_valid = True
    if is_valid:
        water -= needed_water
        total_fire += needed_water
        effort += needed_water * 0.25
        cells.append(needed_water)
print("Cells:")
for cell in cells:
    print(f" - {cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
