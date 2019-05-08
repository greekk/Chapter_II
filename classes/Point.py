import math


class Point:

    def __init__(self, x=0, y=0):
        self.move(x,y)

    def move(self, x, y):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0,0)

    def calculate_distance(self, other_point):
        return math.sqrt((self.y - other_point.x)**2 + (self.y - other_point.y)**2)

point = Point(6,8)
print(point.x, point.y)

#assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
