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

    def __add__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                b = [sum(i) for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print("Сложение векторов разной длины недопустимо")
        elif isinstance(other, (int, float)):
            b = [i + other for i in self.values]
            return Vector(*b)
        else:
            print(f'Вектор нельзя сложить с {other}')

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.values) == len(other.values):
                b = [i[0] * i[1] for i in zip(self.values, other.values)]
                return Vector(*b)
            else:
                print("Умножение векторов разной длины недопустимо")
        elif isinstance(other, (int, float)):
            b = [i * other for i in self.values]
            return Vector(*b)
        else:
            print(f'Вектор нельзя умножать с {other}')
