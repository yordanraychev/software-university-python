class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"

    def set_x(self, new_x: float):
        self.x = new_x

    def set_y(self, new_y: float):
        self.y = new_y


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
