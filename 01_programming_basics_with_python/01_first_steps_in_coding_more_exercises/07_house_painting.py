height = float(input())
length = float(input())
height_roof = float(input())

litre_green_paint_coverage = 3.4
litre_red_paint_coverage = 4.3

# walls - green paint
area_front_back_walls = height * height * 2
area_door = 1.2 * 2
area_sides = height * length * 2
area_windows = 1.5 * 1.5 * 2
area_walls = area_front_back_walls + area_sides - area_door - area_windows

# roof - red paint
area_sides = height * length * 2
area_front_back_roof = height * height_roof
area_roof = area_sides + area_front_back_roof

green_paint_coverage = area_walls / litre_green_paint_coverage
red_paint_coverage = area_roof / litre_red_paint_coverage

print(f"{green_paint_coverage:.2f}")
print(f"{red_paint_coverage:.2f}")
