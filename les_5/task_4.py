"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


try:
    with open('task_4_input.txt', 'r', encoding="utf-8") as file_handler:
        content = file_handler.readlines()
        for i in content:
            if 'One' in i:
                i = 'Один - 1'
                new_file = open('output_task_4.txt', 'w', encoding='utf-8')
                new_file.writelines(i + '\n')
            elif 'Two' in i:
                i = 'Два - 2'
                new_file = open('output_task_4.txt', 'a', encoding='utf-8')
                new_file.writelines(i + '\n')
            elif 'Three' in i:
                i = 'Три - 3'
                new_file = open('output_task_4.txt', 'a', encoding='utf-8')
                new_file.writelines(i + '\n')
            elif 'Four' in i:
                i = 'Четыре - 4'
                new_file = open('output_task_4.txt', 'a', encoding='utf-8')
                new_file.writelines(i + '\n')
            result = i
            print(result)

except IOError:
    print("An IOError has occurred!")
