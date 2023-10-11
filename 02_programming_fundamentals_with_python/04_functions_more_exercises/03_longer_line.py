def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    length1 = distance(x1, y1, x2, y2)
    length2 = distance(x3, y3, x4, y4)
    if length1 > length2:
        print_line(x1, y1, x2, y2)
    elif length1 < length2:
        print_line(x3, y3, x4, y4)
    else:
        print_line(x1, y1, x2, y2)


def print_line(x1, y1, x2, y2):
    if distance(x1, y1, 0, 0) <= distance(x2, y2, 0, 0):
        start_x = x1
        start_y = y1
        end_x = x2
        end_y = y2
    else:
        start_x = x2
        start_y = y2
        end_x = x1
        end_y = y1
    print(f"({int(start_x)}, {int(start_y)})({int(end_x)}, {int(end_y)})")


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())
x_3 = float(input())
y_3 = float(input())
x_4 = float(input())
y_4 = float(input())
longer_line(x_1, y_1, x_2, y_2, x_3, y_3, x_4, y_4)
