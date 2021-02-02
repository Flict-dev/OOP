s = 'hello'
d = {}
# f = open('123.txt')
try:
    1 / 0
    # execute(f)
    # int('hello')
    # d['key']
    # 1 / 0
    # a+b
# except FileNotFoundError:
#     print('ERROR')
except (KeyError, IndexError):
    print('LookupError')
except ZeroDivisionError:
    print('Zero ERROR')
else:
    print('good')
finally:
    print('end')
    # f.close()
# except ValueError:
#     print('Value ERROR')
# except NameError:
#     print('Name ERROR')
# except LookupError:
#     print('Lookup ERROR')
