"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f'({self.real}{"+" if self.imag > 0 else ""}{self.imag}j)'

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = (self.real * other.real) - (self.imag * other.imag)
        imag = ((self.imag * other.real) + (self.real * other.imag))
        return ComplexNumber(real, imag)


a = ComplexNumber(11, -2)
b = ComplexNumber(10, 7)
print(a * b)
print(complex(11, -2) * complex(10, 7))
print(a+b)
print(complex(11, -2) + complex(10, 7))



