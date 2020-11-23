"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту
ситуацию и не завершиться с ошибкой.
"""


class ZeroDivision(Exception):
    def __init__(self, param):
        self.param = param


try:
    num_1 = int(input('Введите первое число:\n>>>'))
    num_2 = int(input('Введите второе число:\n>>>'))

    if num_2 == 0:
        raise ZeroDivision('Число на 0 делить нельзя!!!')
except ValueError:
    print('Ooo man, you killing me')
except ZeroDivision as err:
    print(err)
else:
    print(num_1/num_2)

