class Square:
    def __init__(self, s):
        self.__side = s
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if self.__area is None:
            self.__area = self.side ** 2
        return self.__area

    @area.deleter
    def area(self):
        self.__side = None


class SquarePer:
    def __init__(self, s):
        self.__side = s
        self.__per = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__per = None

    @property
    def per(self):
        if self.__per is None:
            self.__per = self.__side * 4
        return self.__per
