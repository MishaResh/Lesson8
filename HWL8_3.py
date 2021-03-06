# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только
# чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список с числами
# выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить
# соответствующее сообщение. При этом работа скрипта не должна завершаться.
class InError(Exception):
    def __init__(self, my_inp: str):
        self.my_inp = my_inp

    def __str__(self):
        return f'Вы ввели {self.my_inp} это не число'


my_var = ''
my_list = []
while True:
    try:
        my_var = input('Введите элемент списка ->> ')
        if my_var != 'stop':
            if my_var.isdigit():
                my_list.append(my_var)
            else:
                raise InError(my_var)
        else:
            break
    except InError as err:
        print(err)
print(my_list)
