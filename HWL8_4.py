# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад
# и передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

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
    def out_equipment(s_name: str, s_type: str, q_ty: int, st_eq: dict):
        if len(st_eq) == 0:
            print("Этот склад пуст")
        elif s_type in st_eq:
            if st_eq.get(s_type) >= q_ty:
                st_eq[s_type] = st_eq.get(s_type) - q_ty
                print(f'Отдаем в {s_name} все {q_ty} шт. {s_type}. Еще есть {st_eq.get(s_type)} шт.')
            elif 0 < st_eq.get(s_type) < q_ty:
                print(f'Отдаем в {s_name} все {st_eq.get(s_type)} шт. {s_type}. Больше {s_type} нет.')
                st_eq[s_type] = 0
            else:
                print(f'Оборудования {s_type} на складе нет. Ждем поступлений')
        else:
            print(f'Оборудования {s_type} на складе нет. Ждем поступлений')

    def stock_entry(self, s_type, quantity: int):
        if self.max_count >= quantity:
            self.max_count -= quantity
            self.entry_equipment(s_type, quantity, self.st_equipment)
            print(f'Забираем все {quantity} {s_type}. Еще можем взять {self.max_count} единиц')
        else:
            print(f'Берём {self.max_count} {s_type}. Больше не можем')

    def stock_out(self, s_type, quantity: int, struct_name: str):
        self.out_equipment(struct_name, s_type, quantity, self.st_equipment)

    @property
    def in_stock(self):
        pass


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


printer_1 = m_printer('laser', 'printer', 'HP', 100)
scaner_1 = m_Scan('A4', 'scaner', 'Sony', 150)
copyr_1 = copy_tech('A4', 'copyr', 'Xerox', 80)
stock_1 = StockEq(1, 50, {})
stock_1.stock_entry('printer', 25)
stock_1.stock_entry('scaner', 15)
print(stock_1.st_equipment)
stock_1.stock_out('scaner', 12, 'бухгалтерия')
print(stock_1.st_equipment)
stock_1.stock_entry('scaner', 1)
stock_1.stock_out('scaner', 5, 'бухгалтерия')
print(stock_1.st_equipment)