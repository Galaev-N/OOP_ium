from abc import ABC, abstractmethod
from validate import *


# ============ ИНТЕРФЕЙС 1: Product ============
class Product(ABC):
    def __init__(self, name, price, quantity, producer, cost_price, id, description, comments, mark=3.0, status=0):

        self._name = val_name(name)
        self._price = val_price(price)
        self._quantity = val_quantity(quantity)
        self.producer = val_producer(producer)
        self.__cost_price__ = val_cost_price(cost_price)
        self._id = val_id(id)
        self.description = val_description(description)
        self.comments = val_comments(comments)
        self.mark = mark
        self._status = status
        
    
    @abstractmethod
    def get_price(self):
        """Получить цену товара"""
        pass
    
    @abstractmethod
    def get_name(self):
        """Получить название товара"""
        pass
    
    @abstractmethod
    def is_available(self):
        """Проверить наличие товара (возвращает True/False)"""
        pass
    
    @abstractmethod
    def __str__(self):
        """Строковое представление товара"""
        pass
    
    @abstractmethod
    def order(self, wallet):
        """Оформить заказ на товар. wallet - число (кошелёк). Возвращает строку"""
        pass


# ============ ИНТЕРФЕЙС 2: Catalog ============
class Catalog(ABC):
    def __init__(self, items=None):
        if items is None:
            self._items = []
        elif isinstance(items, list):
            flag = 1
            for i in items:
                if not isinstance(i, Product):
                    flag = 0
            if flag:
                self._items = items
            else: raise ValueError('Неверное содержание списка!')
        else: raise TypeError('Ошибка! неверный формат каталога!')
        
    
    @abstractmethod
    def add(self, product):
        """Добавить товар в каталог. product - объект Product. Возвращает строку"""
        pass
    
    @abstractmethod
    def remove(self, product):
        """Удалить товар из каталога. Возвращает строку"""
        pass
    
    @abstractmethod
    def get_all(self):
        """Получить все товары (возвращает список)"""
        pass
    
    @abstractmethod
    def find_by_id(self, id):
        """Найти товар по ID. Возвращает Product или None"""
        pass
    
    @abstractmethod
    def __len__(self):
        """Вернуть количество товаров (целое число)"""
        pass
    
    @abstractmethod
    def __iter__(self):
        """Вернуть итератор по товарам"""
        pass

class Comparable(ABC):
    """Интерфейс для сравнения объектов"""
    
    @abstractmethod
    def compare_to(self, other):
        """
        Сравнивает текущий объект с другим.
        Возвращает:
        - отрицательное число, если self < other
        - 0, если self == other
        - положительное число, если self > other
        """
        pass


# ============ ИНТЕРФЕЙС 4: Printable ============
