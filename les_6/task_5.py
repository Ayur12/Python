"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить,
что выведет описанный метод для каждого экземпляра.
"""


class Stationery:
    title = 'Названиe'

    def draw(self):
        print(f'Запуск отрисовки')


class Pen:
    def draw(self):
        print(f'Ручка')


class Pencil:
    def draw(self):
        print(f'Карандаш')


class Handle:
    def draw(self):
        print(f'Маркер')


basic = Stationery()
basic.draw()

pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
