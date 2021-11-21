# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class My_komp:
    def __init__(self, mk_real, mk_imag):
        self.mk_real = mk_real
        self.mk_imag = mk_imag

    def __str__(self):
        if self.mk_imag < 0:
            return f'{self.mk_real} - {abs(self.mk_imag)}j'
        elif self.mk_imag > 0:
            return f"{self.mk_real} + {self.mk_imag}j"

    def __add__(self, other):
        if (self.mk_real + other.mk_imag) < 0:
            return f'{self.mk_real + other.mk_imag} - {abs(self.mk_real + other.mk_imag)}j'
        if (self.mk_real + other.mk_imag) > 0:
            return f'{self.mk_real + other.mk_imag} + {self.mk_real + other.mk_imag}j'

    def __sub__(self, other):
        if (self.mk_real - other.mk_imag) > 0:
            return f'{self.mk_real - other.mk_imag} + {self.mk_real - other.mk_imag}j'
        if (self.mk_real - other.mk_imag) < 0:
            return f'{self.mk_real - other.mk_imag} - {abs(self.mk_real - other.mk_imag)}j'

    def __mul__(self, other):
        if (self.mk_real * other.mk_imag + self.mk_imag * other.mk_real) > 0:
            return f'{self.mk_real * other.mk_real - self.mk_imag * other.mk_imag} + {self.mk_real * other.mk_imag + self.mk_imag * other.mk_real}*j'
        if (self.mk_real * other.mk_imag + self.mk_imag * other.mk_real) < 0:
            return f'{self.mk_real * other.mk_real - self.mk_imag * other.mk_imag} - {abs(self.mk_real * other.mk_imag + self.mk_imag * other.mk_real)}*j'


y = My_komp(-4, 3)
print(y)
z = My_komp(5, -2)
print(z)
print(z * y)
