class Cat:

    def hello(self):
        if hasattr(self, 'name'):
            print(f"Hello world from {self.name}")
        else:
            print('nothing')

    def show_breed(self):
        print(f'My breed is {self.breed}')

    def set_value(self, name, breed, age=0):
        self.name = name
        self.age = age
        self.breed = breed
