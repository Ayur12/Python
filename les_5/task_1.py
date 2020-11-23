"""
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


f = open('test.txt', 'w')
user_enter = input('enter your text line\n>>> ')
while user_enter:
    f.writelines(user_enter + '\n')
    user_enter = input('enter your text line\n>>> ')
    if not user_enter:
        break
f.writelines(user_enter)

try:
    with open("test.txt") as f:
        for line in f:
            print(line)
except IOError:
    print("An IOError has occurred!")
