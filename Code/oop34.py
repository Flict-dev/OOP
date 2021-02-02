# Exceptions или исключения
print('Hello, world!')


def third():
    print('start third')
    1 / 0
    print('finish third')


def second():
    print('start second')
    third()
    print('finish second')


def first():
    print('start first')
    try:
        second()
    except ZeroDivisionError:
        print('HANDLING First')
    print('finish first')


first()
