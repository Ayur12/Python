"""3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict."""


while True:
    user_month = input('Введите месяц в виде целого число от 1 до 12>>>\n')
    if user_month.isdigit():
        user_month = int(user_month)
        break
    print('ошибка, попробуйте снова')
winter = {12: 'декабрь', 1: 'январь', 2: 'февраль'}
spring = {3: 'март', 4: 'апрель', 5: 'май'}
summer = {6: 'июнь', 7: 'июль', 8: 'август'}
autumn = {9: 'сентябрь', 10: 'октябрь', 11: 'ноябрь'}
if user_month in winter:
    month = winter.get(user_month)
    print(f'{user_month}-й месяц {month} - это зима.')
elif user_month in spring:
    month = spring.get(user_month)
    print(f'{user_month}-й месяц {month} - это весна.')
elif user_month in summer:
    month = summer.get(user_month)
    print(f'{user_month}-й месяц {month} - это лето.')
elif user_month in autumn:
    month = autumn.get(user_month)
    print(f'{user_month}-й месяц {month} - это осень.')
else:
    print('такого месяца нет')
