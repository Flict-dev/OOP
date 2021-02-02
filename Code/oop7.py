from math import sqrt


class Point:
    list_points = []

    def __init__(self, x=0, y=0):
        self.move_to(x, y)
        Point.list_points.append(self)

    def move_to(self, next_x, next_y):
        self.x = next_x
        self.y = next_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        print(f'X - {self.x} and Y - {self.y}')

    def calc_distance(self, other_point):
        if not isinstance(other_point, Point):
            raise ValueError("Объект не является точкой")
        else:
            return sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
