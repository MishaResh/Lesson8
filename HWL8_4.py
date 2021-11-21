# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class MyInpError(Exception):
    def __init__(self, my_inp):
        self.my_inp = my_inp

    def __str__(self):
        return f'Введенное количество {self.my_inp} оборудования -> не число'


class Office_eq:
    type_eq: str  # тип оргтехники
    brand_eq: str  # производитель оргтехники (IBM)
    price_eq: int  # цена за единицу

    def __init__(self, type_eq, brand_eq, price_eq):
        self.type_eq = type_eq
        self.brand_eq = brand_eq
        self.price_eq = price_eq


class StockEq:
    stock_ed: int  # идентификатор склада
    max_count: int  # максимальное количество единиц оргтехники
    st_equipment: dict  # количество по типам

    def __init__(self, stock_ed, max_count, st_equipment):
        self.st_equipment = st_equipment
        self.max_count = max_count
        self.stock_ed = stock_ed

    @staticmethod
    def entry_equipment(s_type: str, q_ty: int, st_eq: dict):
        if len(st_eq) == 0:
            st_eq.update({s_type: q_ty})
        elif s_type in st_eq:
            st_eq[s_type] = st_eq.get(s_type) + q_ty
        else:
            st_eq.update({s_type: q_ty})

    @staticmethod
    def out_equipment(s_name: str, s_type: str, q_ty: int, st_eq: dict, st_mc: int):
        if len(st_eq) == 0:
            print(f'Этот склад пуст')
        elif s_type in st_eq:
            if st_eq.get(s_type) >= q_ty:
                st_eq[s_type] = st_eq.get(s_type) - q_ty
                st_mc = st_mc + q_ty
                print(f'Отдаем в {s_name} все {q_ty} шт. {s_type}. Еще есть {st_eq.get(s_type)} шт.')
            elif 0 < st_eq.get(s_type) < q_ty:
                print(f'Отдаем в {s_name} все {st_eq.get(s_type)} шт. {s_type}. Больше {s_type} нет.')
                st_mc = st_mc + st_eq.get(s_type)
                st_eq[s_type] = 0
            else:
                print(f'Оборудования {s_type} на складе нет. Ждем поступлений')
        else:
            print(f'Оборудования {s_type} на складе нет. Ждем поступлений')
        return st_mc

    def stock_entry(self):
        y = True
        while y == True:
            s_type = input('Что принимаем на склад ')
            quantity = input(f'Сколько {s_type} принимаем на склад ')
            try:
                if quantity.isdigit():
                   quantity = int(quantity)
                   if self.max_count >= quantity:
                       self.max_count -= quantity
                       self.entry_equipment(s_type, quantity, self.st_equipment)
                       print(f'Забираем все {quantity} {s_type}. Еще можем взять {self.max_count} единиц')
                       y = False
                   else:
                       print(f'Берём {self.max_count} {s_type}. Больше не можем')
                       y = False
            except MyInpError(quantity) as err:
                print(err)

    def stock_out(self):
        x = True
        while x == True:
            s_type = input('Что отдаем со склада ')
            quantity = input(f'Сколько {s_type} отдаем ')
            struct_name = input('Куда отдаем')
            try:
                if quantity.isdigit():
                    quantity = int(quantity)
                    self.max_count = self.out_equipment(struct_name, s_type, quantity, self.st_equipment,
                                                        self.max_count)
                    x = False
                else:
                    raise MyInpError(quantity)
            except TypeError as err:
                print(err)

    @property
    def stock_leftovers(self):
        print(f'На складе № {self.stock_ed} хранятся \n {self.st_equipment} \n свободно {self.max_count} мест')

class m_printer(Office_eq):
    print_type: str

    def __init__(self, print_type, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, brand_eq, price_eq)
        self.print_type = print_type


class m_Scan(Office_eq):
    scan_format: str

    def __init__(self, scan_format, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, brand_eq, price_eq)
        self.scan_format = scan_format


class copy_tech(Office_eq):
    copy_format: str

    def __init__(self, copy_format, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, brand_eq, price_eq)
        self.copy_format = copy_format


# s_type = input('Введите номер склада ->')
# s_type = input('Введите номер склада ->')


printer_1 = m_printer('laser', 'printer', 'HP', 100)
scaner_1 = m_Scan('A4', 'scaner', 'Sony', 150)
copyr_1 = copy_tech('A4', 'copyr', 'Xerox', 80)
stock_1 = StockEq(1, 50, {})
stock_1.stock_entry()
# stock_1.stock_entry()
print(stock_1.st_equipment)
stock_1.stock_out()
print(stock_1.st_equipment)
# stock_1.stock_entry()
# stock_1.stock_out()
# print(stock_1.st_equipment)
stock_1.stock_leftovers
