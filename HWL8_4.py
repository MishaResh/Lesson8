# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс
# «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
class Office_eq:
    type_eq: str  # тип оргтехники
    brand_eq: str  # производитель оргтехники (IBM)
    price_eq: int  # цена за единицу

    def __init__(self, type_eq, brand_eq, price_eq):
        self.type_eq = type_eq
        self.brand_eq = brand_eq
        self.price_eq = price_eq


class Stock_eq:
    stock_ed: int  # идентификатор склада
    max_count: int  # максимальное количество единиц оргтехники
    st_equipment: dict  # количество по типам

    def __init__(self, stock_eq, max_count, st_equipment):
        self.st_equipment = st_equipment
        self.max_count = max_count
        self.stock_ed = stock_eq


class m_printer(Office_eq):
    print_type: str

    def __init__(self, print_type, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, brand_eq, price_eq)
        self.print_type = print_type


class m_Scan(Office_eq):
    scan_format: str

    def __init__(self, scan_format, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, type_eq, brand_eq, price_eq)
        self.scan_format = scan_format


class copy_tech(Office_eq):
    copy_format: str

    def __init__(self, copy_format, type_eq, brand_eq, price_eq):
        super().__init__(type_eq, type_eq, brand_eq, price_eq)
        self.copy_format = copy_format


printer_1 = m_printer('laser', 'printer', 'HP', 100)
