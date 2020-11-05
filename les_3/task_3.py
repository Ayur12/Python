"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func():
    try:
        arg_1 = float(input("Введите первое число\n>>> "))
        arg_2 = float(input("Введите второе число\n>>> "))
        arg_3 = float(input("Введите третье число\n>>> "))
    except ValueError:
        return
    args = [arg_1, arg_2, arg_3]
    args.sort()
    result = args[1] + args[2]
    print(result)


my_func()
