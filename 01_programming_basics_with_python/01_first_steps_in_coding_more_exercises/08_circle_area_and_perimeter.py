import math
from math import pi

radius = float(input())

calculated_area = radius * radius * pi
calculated_perimeter = 2 * radius * pi

print(f"{calculated_area:.2f}")
print(f"{calculated_perimeter:.2f}")
