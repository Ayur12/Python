"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""


class Road:

    def _s_road(self, lenght, width):
        self.lenght = float(lenght)
        self.width = float(width)
        return lenght * width


class Tons(Road):
    def _asphalt(self, mass, depth):
        self.mass = float(mass)
        self.depth = float(depth)
        return mass * depth


a = Tons()
print((a._s_road(20, 50) * a._asphalt(25, 5)))
