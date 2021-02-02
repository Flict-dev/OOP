class Money:
    def __init__(self, dollars, cents):
        self.total_cents = int(dollars) * 100 + int(cents)

    def __str__(self):
        return f"Ваше состояние составляет {int(self.total_cents // 100)} долларов {self.total_cents % 100} центов"

    @property
    def dollars(self):
        return self.total_cents // 100

    @dollars.setter
    def dollars(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.total_cents = new_value * 100 + (self.total_cents - (self.total_cents // 100)*100)
        else:
            print("Error dollars")

    @property
    def cents(self):
        return self.total_cents % 100

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:
            self.total_cents = (self.total_cents - (self.total_cents % 100) + value)
        else:
            print("Error cents")
