# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class MData:
    my_data = str

    def __init__(self, my_data):
        self.my_data = my_data

    @staticmethod
    def val_data(my_data: str):
        my_data_l = []

        if my_data[:2].isdigit() and 1 <= int(my_data[:2]) <= 31:
            my_data_l.append(my_data[:2])
        else:
            my_data_l.append('**')
        if my_data[my_data.find('-') + 1:my_data.find('-') + 3].isdigit() and 1 <= int(
                my_data[my_data.find('-') + 1:my_data.find('-') + 3]) <= 12:
            my_data_l.append(my_data[my_data.find('-') + 1:my_data.find('-') + 3])
        else:
            my_data_l.append('**')
        if my_data[len(my_data) - 4:len(my_data)].isdigit():
            my_data_l.append(my_data[len(my_data) - 4:len(my_data)])
        else:
            my_data_l.append('**')

        return my_data_l

    @classmethod
    def my_str(cls, my_data: str):
        dd, mm, yy = int, int, int
        try:
            dd = int(cls.val_data(my_data)[0])
            mm = int(cls.val_data(my_data)[1])
            yy = int(cls.val_data(my_data)[2])
        except ValueError:
            print('Ошибка! Не число, или ошибка в дате')
            exit()
        else:
            return f'Число - {dd} его тип {type(dd)}, Месяц - {mm} его тип {type(mm)} Число - {yy} его тип {type(yy)}'


print(MData.my_str('31-12-2021'))
print(MData.my_str('44-12-2021'))
print(MData.my_str('ии-12-2021'))
