class MyException(Exception):
    """this is my Exception"""

    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return f'MyException ({self.message})'
        else:
            return 'MyException is empty'


try:
    raise MyException('hello', 1, 2, 3)
except MyException:
    print('done')


class SnakeExceptionBase(Exception):
    """Основной класс ошибок змейки"""


class SnakeBorder(SnakeExceptionBase):
    """Ошибка соприкосновения змеи со стенкой"""


class SnakeTailException(SnakeExceptionBase):
    """Ошибка соприкосновения змеи и тела"""
