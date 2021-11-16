# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.


def p_data(my_data: str):
    print(f'p_data = {my_data}')
    return True if my_data[:2].isdigit() else print('фигня')


class Дата:
    my_data = str
    @staticmethod
    def my_str(my_data: str):
        dd = int(my_data[:2])
        mm = int(my_data[my_data.find('-')+1:my_data.find('-',)+3])
        yy = int(my_data[len(my_data)-4:len(my_data)])
        return f'День -{dd} тип {type(dd)} Месяц - {mm} тип {type(mm)} Год - {yy} тип {type(yy)}'
    @classmethod
    def isvlec(cls, my_data: str):
        return True if my_data[:2].isdigit() else print('фигня')


print(Дата.my_str('22-10-2021'))
