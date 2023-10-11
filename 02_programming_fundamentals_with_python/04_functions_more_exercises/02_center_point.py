from math import floor


def find_closest_coordinates(x, y, xx, yy):
    if abs(x) + abs(y) <= abs(xx) + abs(yy):
        return f"({x}, {y})"
    return f"({xx}, {yy})"


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
print(find_closest_coordinates(x1, y1, x2, y2))
