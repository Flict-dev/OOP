# Инструкция raise


# try:
#     1 / 0
# except (KeyError, IndexError) as error:
#     print(f"Logging error: {repr(error)}")
#     raise
# except ZeroDivisionError as err:
#     print(f"Logging error: {err} {repr(err)}")
#     raise TypeError('!' * 10)  # from None

try:
    raise ValueError('Ошибка значеня')
except ValueError as first:
    try:
        raise TypeError('Ошибка типа')
    except TypeError as second:
        raise Exception("Большое исключение")  # from None or first or second
