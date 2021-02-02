# slots также унаследует все атрибуты из родительского класса,
# но монжно задать ещё или создать пустую коллекцию

class Rectangle:
    __slots__ = ('__width', 'height')

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        print('setter called')
        self.__width = value


class Square(Rectangle):
    __slots__ = ('color')

    def __init__(self, a, b, color):
        super().__init__(a, b)
        self.color = color
