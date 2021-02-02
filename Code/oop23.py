class Vector:
    def __init__(self, *args):
        self.values = list(args)

    def __repr__(self):
        return str(self.values)

    def __getitem__(self, item):
        if 0 <= item <= len(self.values):
            return self.values[item]
        else:
            raise IndexError("Индекс за пределами коллекции")

    def __setitem__(self, key, value):
        if 0 <= key <= len(self.values):
            self.values[key] = value
        elif key > len(self.values):
            dif = key - len(self.values) + 1
            self.values.extend([0] * dif)
            self.values[key] = value  # но можно отнимать 1 от key
        else:
            raise IndexError("Индекс за пределами коллекции")

    def __delitem__(self, key):
        if 0 <= key <= len(self.values):
            del self.values[key]
        else:
            raise IndexError("Индекс за пределами коллекции")
