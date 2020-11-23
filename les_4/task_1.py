"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


from sys import argv
script_name, hours, rate, bonus = argv
hours = float(hours)
rate = float(rate)
bonus = float(bonus)


def wage_func(hours, rate, bonus):
    result = hours * rate + bonus
    print(result)


wage_func(hours, rate, bonus)
