"""
4.Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
"""

import random


class Car:
    speed = random.randint(1, 100)
    color = random.choice(['black', 'white', 'red', 'blue', 'yellow'])
    name = random.choice(['TownCar', 'SportCar', 'WorkCar', 'PoliceCar'])
    is_police = random.choice([True, False])

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self):
        direction = random.choice(['Налево', 'Направо'])
        print(direction)

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        max_speed = 60
        if self.speed > max_speed:
            print(f'Ваша скорость {self.speed}. Сбросьте скорость до 60 км/ч.')
        elif 0 < self.speed < 60:
            print(f'Ваша скорость {self.speed}')


class SportCar(Car):
    def model_car(self):
        return self.name


class WorkCar(Car):
    def show_speed(self):
        max_speed = 40
        if self.speed > max_speed:
            print(f'Ваша скорость {self.speed}. Сбросьте скорость до 40 км/ч.')
        elif 0 < self.speed < 60:
            print(f'Ваша скорость {self.speed}')


class PoliceCar(Car):
    def police(self):
        if self.is_police == True:
            print('Это полицейская машина')
        else:
            print('Это не полицейская машина')

car = Car()
car.turn()
car.turn()

bus = TownCar()
bus.show_speed()
print(f'Цвет автобуса {bus.color}')

sport = SportCar()
print(f'Вы выбрали {sport.name}')
sport.go()
sport.show_speed()
cop = PoliceCar()
cop.police()
