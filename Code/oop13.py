class Example:
    def hello():
        print('Hello, world!')

    def instance_hello(self):
        print(f'Hello, world{self}')

    @staticmethod  # Не привязан не к классу, не к объекту
    def static_hello():
        print('static_hello!')

    @classmethod  # Привязан к классу объекта и к классу в принципе
    def class_hello(cls):
        print(f'class_hello {cls}')
