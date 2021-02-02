class Person:
    def __init__(self, name, surname, gender='male'):
        self.name = name
        self.surname = surname
        if gender not in ('male', 'female'):
            print("Не знаю, что вы имели ввиду? Пусть это будет мальчик!")
            self.gender = 'male'
        else:
            self.gender = gender

    def __str__(self):
        if self.gender == 'male':
            return f'Гражданин {self.surname} {self.name}'
        else:
            return f'Гражданка {self.surname} {self.name}'


class Vector:
    def __init__(self, *args):
        self.values = []
        for item in args:
            if isinstance(item, int):
                self.values.append(item)
        self.values = sorted(self.values)

    def __str__(self):
        if len(self.values) == 0:
            return "Пустой вектор"
        return f'Вектор{tuple(self.values)}'
