quantity = int(input())
days = int(input())
ornament, skirt, garland, lights = 2, 5, 3, 15
total_cost, spirit = 0, 0
for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += ornament * quantity
        spirit += 5
    if day % 3 == 0:
        total_cost += (skirt + garland) * quantity
        spirit += 13
    if day % 5 == 0:
        total_cost += lights * quantity
        spirit += 17
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_cost += skirt + garland + lights
if days % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_cost}")
print(f"Total spirit: {spirit}")
