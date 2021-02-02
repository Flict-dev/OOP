# Делегирование - функция super() вызывается к родительскому классу
class Person:  # Parent

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def breathe(self):
        print('Человек дышит')

    def __str__(self):
        return f'Person {self.name} and {self.surname}'

    def info(self):
        print('Parent class')
        print(self)


class Doctor(Person):  # subclass

    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self):
        return f'Doctor {self.name} {self.surname} and {self.age}'

    def breathe(self):
        print('Доктор дышит')
        super().breathe()


p = Person('Ivan', 'Ivanov')
d = Doctor('Petr', 'Petrov', 25)
d.breathe()
d.info()
