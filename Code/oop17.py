# add - '+', mul - '*', sub - '-', truediv - '/'.
class BankAccount:
    def __init__(self, name, balance):
        print('New object')
        self.name = name
        self.balance = balance

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return BankAccount(self.name, self.balance + other)
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise NotImplemented

    def __repr__(self):
        return f" Клиент {self.name} с балансом {self.balance}"

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return self.balance * other
        if isinstance(other, BankAccount):
            return self.balance * other.balance
        if isinstance(other, str):
            return self.name + other
        raise NotImplemented
