from timeit import timeit


# slots помогает оставить только необходимые атрибуты, ускорить код и уменьшить объем памяти

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def make_cl1():
    l = Point(5, 6)
    l.x = 10
    del l.y


def make_cl2():
    l = PointSlots(5, 6)
    l.x = 10
    del l.y


s = Point(2, 4)
print(s.__sizeof__(), s.__dict__.__sizeof__())
d = PointSlots(5, 6)
print(d.__sizeof__())
print(timeit(make_cl1))
print(timeit(make_cl2))
