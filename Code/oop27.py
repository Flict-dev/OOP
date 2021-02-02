class Person:  # Parent
    def __init__(self, name):
        self.name = name

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')

    def ability(self):
        pass

    def combo(self):
        self.can_breathe()
        self.can_walk()
        self.ability()

    def __str__(self):
        return f'Person {self.name}'


class Doctor(Person):  # subclass
    def ability(self):
        print('Я могу лечить')

    def __str__(self):
        return f'Doctor {self.name}'


p = Person('John')
d = Doctor('Max')
d.combo()
