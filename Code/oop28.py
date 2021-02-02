class Person:  # Parent

    def can_breathe(self):
        print('Я могу дышать')

    def can_walk(self):
        print('Я могу ходить')

    def combo(self):
        self.can_breathe()
        self.can_walk()
        if hasattr(self, 'ability'):
            self.ability()


class Doctor(Person):  # subclass
    def ability(self):
        print('Я могу лечить')


p = Person()
d = Doctor()
p.combo()
print('-' * 10)
d.combo()
