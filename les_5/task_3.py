"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


try:
    with open('task_3.txt', 'r', encoding="utf-8") as file_handler:
        salary = []
        workers = []
        my_list = file_handler.read().split('\n')
        for el in my_list:
            el = el.split()
            if int(el[1]) < 20000:
                workers.append(el[0])
            salary.append(el[1])
    print(f'Оклад меньше 20 тыс., получают {workers}, средний доход {sum(map(int, salary)) / len(salary)}')
except IOError:
    print("An IOError has occurred!")
