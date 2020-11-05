user_number = int(input('Введите число любое положительное число: '))
max_number = user_number % 10  # предположим что последняя цифра и есть максимальное число
user_number = user_number // 10  # поскольку последнюю цифру мы учли, то избавимся от нее

"' далее в цикле будем извлекать с конца числа каждую его цифру и сравнивать со значением max" \
"и если очередная цифра больше, то будем присваивать ее переменной max'"

while user_number > 0:
    if user_number % 10 > max_number:
        max_number = user_number % 10
    user_number = user_number // 10

print(max_number)
