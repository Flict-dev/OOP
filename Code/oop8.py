class Cat:
    __shared_attr = {
        'bred': 'pers',
        'color': 'white'
    }

    def __init__(self):
        self.__dict__ = Cat.__shared_attr
