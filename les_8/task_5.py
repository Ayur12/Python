"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
данных, можно использовать любую подходящую структуру, например словарь.
"""
class Storage:
    def __init__(self, city, name, address):
        self.city = city
        self.name = name
        self.address = address

    def acceptance(self):
        pass


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