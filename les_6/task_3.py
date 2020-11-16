"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).
"""


class Worker:
    name = 'John'
    surname = 'Smith'
    position = 'Киллер'
    _income = {'wage': 100000, 'bonus': 30000}


class Position(Worker):
    def get_full_name(self):
        return f'{self.position} {self.name} {self.surname}'

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        return total


worker = Position()
print(f'{worker.get_full_name()} получает {worker.get_total_income()} долларов')
