"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
class Data:
    def __init__(self, date):
        self.date = date

    def __str__(self):
        return self.date

    @classmethod
    def get_date(cls, date: str):
        try:
            return tuple(map(int, date.split('-')))
        except ValueError:
            return 'Некорректные данные'


    @staticmethod
    def get_value(data):
        if not type(data) == str:
            data == str(data)
        day, month, year = [i for i in Data.get_date(data)]
        m30 = (4, 6, 9, 11)
        m31 = (1, 3, 5, 7, 8, 10, 12)

        if 0 <= year <=2020 and 0 <= month <= 12:
            if (month in m31 and day <= 31) or (month in m30 and day <=30):
                return True
            elif month == 2:
                if year % 4 or (not year % 100 and year % 400):
                    return day <= 28
                else:
                    return day <=29
        return False


if __name__ == '__main__':
    print(Data.get_date('12-10-1987'))
    print(Data.get_date('12-10-198a'))

    date_1 = Data('31-10-1987')
    print(date_1, '->', Data.get_value(str(date_1)))



