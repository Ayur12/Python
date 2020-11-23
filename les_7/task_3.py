"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()),
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны применяться только к
клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
 нуля, иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
 двух клеток.
Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
 Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
*****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class Cell:

    def __init__(self, count_cell):
        self.count_cell = int(count_cell)

    def __add__(self, other):  # сложение
        return Cell(self.count_cell + other.count_cell)

    def __sub__(self, other):  # вычитание
        if self.count_cell < other.count_cell:
            print('Разность двух клеток должна быть больше нуля')
            return None
        else:
            return Cell(self.count_cell - other.count_cell)

    def __mul__(self, other):  # умножение
        return Cell(self.count_cell * other.count_cell)

    def __truediv__(self, other):  # деление
        return Cell(self.count_cell // other.count_cell)

    def make_order(self, count_in_line):
        lines = self.count_cell//count_in_line
        last_line = self.count_cell%count_in_line
        el = ''
        for _ in range(lines):
            el = el + '*'*count_in_line+'\n'
        if last_line:
            el = el + '*'*last_line
        return el


a = Cell(15)
b = Cell(10)
c = a + b
print(c.count_cell)
c = c - Cell(2)
print(c.count_cell)
c = c * b
print(c.count_cell)
c = c / b
print(c.count_cell)
print(Cell.make_order(c, 5))
