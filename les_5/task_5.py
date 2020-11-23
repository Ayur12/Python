"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""
string = '1 33 32 4 5 6 7 250 9 10'
try:
    with open('task_5.txt', 'w', encoding="utf-8") as file_handler:
        content = file_handler.writelines(string)

except IOError:
    print("An IOError has occurred!")


try:
    with open('task_5.txt', 'r', encoding="utf-8") as file_handler:
        content = list(file_handler.readlines())
        sum_list = []
        for el in content:
            new_list = el.split()
            for num in new_list:
                num = int(num)
                sum_list.append(num)
        print(sum(sum_list))
except IOError:
    print("An IOError has occurred!")
