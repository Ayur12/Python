"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""


class Car:
    speed = 'speed'
    color = 'color'
    name = 'name'
    is_police = True
    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self):
        print('машина повернула налево')
        print('машина повернула направо')
    def show_speed(self):
        print('Текущая скорость')


class TownCar(Car):
    def show_speed(self):
        print('Текущая скорость')


class SportCar(Car):
    def show_speed(self):
        print('Текущая скорость')


class WorkCar(Car):
    def show_speed(self):
        print('Текущая скорость')


class PoliceCar(Car):
    def show_speed(self):
        print('Текущая скорость')