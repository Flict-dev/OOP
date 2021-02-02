# Основные приципы наследования
class Person:  # Parent

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')


class Doctor(Person):  # subclass
    def ability(self):
        print('Я могу лечить')


class Programmer(Person):  # subclass
    def ability(self):
        print('Я могу кодить')


a = Programmer()

b = Doctor()
