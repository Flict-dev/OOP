class Marks:
    def __init__(self, values):
        self.value = values

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        print('!')
        if self.index >= len(self.value):
            raise StopIteration
        letter = self.value[self.index]
        self.index += 1
        return letter


class Student:

    def __init__(self, name, surname, marks):
        self.name = name
        self.surname = surname
        self.marks = marks

    def __iter__(self):
        self.index = 0
        return iter(self.marks)

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


m = Marks([9, 6, 7, ])
igor = Student('Igor', 'Nicolaev', m)

for i in igor:
    print(i)
