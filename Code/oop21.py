from time import perf_counter


class Counter:
    def __init__(self):
        self.counter = 0
        self.summa = 0
        self.length = 0
        print('init object', self)

    def __call__(self, *args, **kwargs):
        self.counter += 1
        self.summa += sum(args)
        self.length += len(args)
        print(f'Наш экземпляр вызывался {self.counter} раз')


class Timer:
    def __init__(self, fn):
        self.fn = fn

    def __call__(self, *args, **kwargs):
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        finish = perf_counter()
        print(f'Время - {finish - start}')
        return result


@Timer
def fact(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr
