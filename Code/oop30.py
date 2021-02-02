class Doctor:
    def __init__(self, degree):
        self.degree = degree

    def ability(self):
        print("I'm doctor, i can cure")

    def can_build(self):
        print("I'm builder, i can build but bad")


class Builder:

    def __init__(self, rank):
        self.rank = rank

    def ability(self):
        print("I'm builder, i can build")


class Person(Doctor, Builder):
    def __init__(self, degree, rank):
        super().__init__(degree)
        Builder.__init__(self, rank)

    def __str__(self):
        return f"Person -  {self.degree}, {self.rank}"


p = Person('spec', 5)
print(p)
