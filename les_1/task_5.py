proceeds = int(input('Введите вашу выручку в рублях: '))
cost = int(input('Введите издержки фирмы: '))
profitability_proceeds = proceeds / cost
profit = proceeds - cost
if proceeds > cost:
    print('Фирма приносит прибыль!')
else:
    print('Ваша фирма убыточна, работайте усерднее.')
print(f'Коэффициент рентабельности выручки вашей фирмы составляет {profitability_proceeds}')

number_employees = int(input('Введите количество сотрудников фирмы: '))
profit_employee = profit / number_employees
print(f'В среднем один сотрудник приносит прибыль фирме в размере {profit_employee} руб.')

