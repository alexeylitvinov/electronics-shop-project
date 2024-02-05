import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.total_price = None
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        """
        Сложение атрибута quantity экземпляров класса Item и его дочерних классов
        """
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты класса Item и его наследников')
        return self.quantity + other.quantity

    @classmethod
    def instantiate_from_csv(cls, path_file):
        """
        Создание экземпляров класса через .csv файл
        """
        Item.all = []
        with open(path_file) as file:
            reader = csv.DictReader(file)
            for i in reader:
                name, price, quantity = i['name'], i['price'], i['quantity']
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(num: str):
        """
        Статический метод, возвращающий число из числа-строки
        """
        if num.count('.'):
            num.split('.')
            return int(num[0])
        return int(num)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_string: str):
        """
        Сеттер имени. Если длинна имени больше 10 символов, обрезаем до 10
        """
        self.__name = name_string
        if len(name_string) > 10:
            self.__name = name_string[:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.total_price = self.price * self.quantity
        return self.total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
