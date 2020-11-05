"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division_func():
    try:
        user_num1 = float(input("Введите первое число\n>>> "))
        user_num2 = float(input("Введите второе число\n>>> "))
    except ValueError:
        return
    if user_num2 == 0:
        print("Число на 0 делить нельзя")
    else:
        return user_num1 / user_num2


print(division_func())
