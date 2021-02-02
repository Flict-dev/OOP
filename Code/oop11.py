class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def my_balance(self):
        print('get_balance')
        return self.__balance

    @my_balance.setter
    def my_balance(self, value):
        print('set_balance')
        if isinstance(value, (int, float)):
            self.__balance = value
        else:
            raise ValueError("Здесь должно быть число")

    @my_balance.deleter
    def my_balance(self):
        print('delete_balance')
        del self.__balance
    # my_balance = my_property_balance.setter(my_balance)
    # my_balance = property(my_balance)
    # my_balance = my_balance.setter(set_balance)
    # my_balance = my_balance.deleter(delete_balance)
