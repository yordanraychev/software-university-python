from math import ceil, floor

area_vineyard = int(input())
grapes_per_square = float(input())
needed_litres = int(input())
staff = int(input())

grapes_production = area_vineyard * grapes_per_square * 0.4
litres_produced = grapes_production / 2.5
difference = abs(needed_litres - litres_produced)
remainder = (litres_produced - needed_litres) / staff

if litres_produced < needed_litres:
    print(f"It will be a tough winter! More {floor(difference)} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {floor(litres_produced)} liters.")
    print(f"{ceil(difference)} liters left -> {ceil(remainder)} liters per person.")
    