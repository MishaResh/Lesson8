# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его
# работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа
# должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class InError(Exception):
    def __init__(self, my_inp):
        self.my_inp = my_inp

    def __str__(self):
        return f'Ваш знаменатель = {my_inp_2} деление на 0 невозможно'

while True:
    try:
        my_inp_1 = int(input('Введите делимое ->'))
        my_inp_2 = int(input('Введите делитель ->'))
        if my_inp_2 == 0:
            raise InError(my_inp_2)
    except ValueError:
        print("Вы ввели не число")
        break
    except InError as err:
        print(err)
        break
    else:
        print(f"Все хорошо. Ваш результат: {my_inp_1/my_inp_2}")