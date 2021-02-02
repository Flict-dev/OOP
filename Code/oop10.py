class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def get_balance(self):
        print('get_balance')
        return self.__balance

    def set_balance(self, value):
        print('set_balance')
        if isinstance(value, (int, float)):
            self.__balance = value
        else:
            raise ValueError("Здесь должно быть число")

    def delete_balance(self):
        print('delete_balance')
        del self.__balance

    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
