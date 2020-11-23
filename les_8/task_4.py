"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class Storage:
    def __init__(self, city, name, address):
        self.city = city
        self.name = name
        self.address = address

class OfficeEquipment:
    def __init__(self, brand, series):
        self.brand = brand
        self.series = series



class Printer(OfficeEquipment):

    color = 'yes'
    type = 'laser'



class Scanner(OfficeEquipment):
    pc_compatibility = 'yes'
    paper_size = 'a4'


class Copier(OfficeEquipment):
    copy_speed = 14
    auto_copying = 'no'
