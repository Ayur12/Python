result_first_day = int(input('Введите сколько километров вы пробежали в первый день: '))
number_km = int(input('Километраж'))
day = 1
while result_first_day < number_km:
    result_first_day = result_first_day * 1.1
    day += 1
    print(f'{day}-й день: {round(result_first_day, 2)}')

print(f'{number_km} км вы сможете пробежать на {day}-й день')
