"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""


try:
    f = open("task_2.txt", "r")
    quantity_lines = f.readlines()
    print(f'Количество строк в файле {len(quantity_lines)}')
    for line, value in enumerate(quantity_lines):
        print(f'Строка {line + 1}, количество слов в строке {len(value.split())}')
except IOError:
    print("An IOError has occurred!")
finally:
    f.close()
