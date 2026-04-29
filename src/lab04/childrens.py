
from interfaces import Product, Catalog
import random
from validate import *

# ============ РЕАЛИЗАЦИЯ Product в классе Food ============
class Food(Product):
    def __init__(self, name, price, quantity, producer, cost_price, id, description, comments, expiration_days, calories=0, mark=3.0, status=0):
        super().__init__(name, price, quantity, producer, cost_price, id, 
                        description, comments, mark, status)
        
        self.calories = val_calories(calories)
        self._expiration_days = val_per(expiration_days)
    
    # Реализация абстрактных методов Product
    def get_price(self):
        return self._price if self._status != 1 else self._price * 1.22
    
    def get_name(self):
        return self._name
    
    def is_available(self):
        return self._quantity > 0 and self._status != 1
    
    def order(self, wallet):
        if not self.is_available():
            return f'Отказ! Товара "{self._name}" нет в наличии'
        if wallet >= self.get_price():
            self._quantity -= 1
            return f'Отлично! Товар "{self._name}" успешно заказан!'
        else:
            need = self.get_price() - wallet
            return f'Отказ! Недостаточно {need} рублей на балансе'
    
    def __str__(self):
        if self._status == 1:
            return 'Информация о продукте временно недоступна'
        status = "В наличии" if self.is_available() else "Нет в наличии"
        return f'{self._name} | {self._price} руб. | {status} | Срок годности: {self._expiration_days} дней'
    
    # Специфичные для Food методы
    def check_expiration(self):
        if self._expiration_days <= 0:
            return 'ПРОСРОЧЕНО!'
        else:
            return f'Свежий продукт. Годен {self._expiration_days} дней'


# ============ РЕАЛИЗАЦИЯ Product в классе Techic ============
class Techic(Product):
    def __init__(self, name, price, quantity, producer, cost_price, id, description, comments, warranty_months, power_consumption, mark, status):
        super().__init__(name, price, quantity, producer, cost_price, id, 
                        description, comments, mark, status)
        self.warranty_months = val_months(warranty_months)
        self.power_consumption = val_power(power_consumption)
    
    # Реализация абстрактных методов Product (другая логика!)
    def get_price(self):
        # Техника может иметь сезонную скидку
        if self._status == 1:
            return self._price * 1.15
        return self._price
    
    def get_name(self):
        return self._name
    
    def is_available(self):
        return self._quantity > 0 and self._status != 1
    
    def order(self, wallet):
        # Техника требует проверки гарантии при заказе
        if not self.is_available():
            return f'Отказ! Техники "{self._name}" нет в наличии'
        if wallet >= self.get_price():
            self._quantity -= 1
            return f'Техника "{self._name}" заказана! Гарантия {self._warranty_months} мес.'
        else:
            need = self.get_price() - wallet
            return f'Недостаточно средств. Нужно еще {need} руб.'
    
    def __str__(self):
        if self._status == 1:
            return 'Информация о технике временно недоступна'
        status = "В наличии" if self.is_available() else "Нет в наличии"
        return f'{self._name} | {self.get_price()} руб. | {status} | Гарантия: {self._warranty_months} мес.'
    
    # Специфичный метод
    def check_price_online(self):
        results = ["Вы нашли дешевле!", "Цена адекватная", "РКН блокирует площадку..."]
        return random.choice(results)


# ============ РЕАЛИЗАЦИЯ Product в классе Estate ============
class Estate(Product):
    def __init__(self, name, price, producer, id, description, comments, location, area, mark, free=1):
        super().__init__(
            name=name,           # название
            price=price,         # цена
            quantity=1,          # количество (для недвижимости обычно 1 объект)
            producer=producer,   # производитель/застройщик
            cost_price=price * 0.7,  # себестоимость (можно рассчитать или передать отдельно)
            id=id,               # идентификатор
            description=description,  # описание
            comments=comments,   # комментарии
            mark=mark            # оценка
        )
        self.location = val_loc(location)
        self.proportions = val_prop(area)
        self.free = free
    
    def get_price(self):
        if self._status == 1:
            return self._price * 1.1
        return self._price
    
    def get_name(self):
        return self._name
    
    def is_available(self):
        return self._free == 1 and self._status != 1
    
    def order(self, wallet):
        if not self.is_available():
            return f'Отказ! Объект "{self._name}" {"занят" if self._free == 0 else "недоступен"}'
        if wallet >= self.get_price():
            self._free = 0
            return f'Поздравляем! Недвижимость "{self._name}" снята!'
        else:
            need = self.get_price() - wallet
            return f'Не хватает {need} руб. :('
    
    def __str__(self):
        if self._status == 1:
            return 'Информация об объекте временно недоступна'
        status = "СВОБОДНО" if self._free == 1 else "ЗАНЯТО"
        return f'{self._name} | {self.get_price()} руб. | {status} | {self._area} кв.м. | {self._location}'


# ============ РЕАЛИЗАЦИЯ Catalog ============
class ProductCatalog(Catalog):
    def __init__(self, items=None):
        super().__init__(items)
    
    def add(self, product):
        self._items.append(product)
        return f'Товар "{product.get_name()}" добавлен в каталог'
    
    def remove(self, product):
        if product in self._items:
            self._items.remove(product)
            return f'Товар "{product.get_name()}" удалён'
        else:
            return f'Товар "{product.get_name()}" не найден'
    
    def get_all(self):
        return self._items  # возвращаем копию
    
    def find_by_id(self, id):
        for product in self._items:
            if hasattr(product, '_id') and product._id == id:
                return product
        return None
    
    def __len__(self):
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)
    
    # Дополнительные методы
    def get_available(self):    
        available = []
        for product in self._items:
            if product.is_available():
                available.append(product)
        return available
    
    def sort_by_price(self):
        """Отсортировать по цене"""
        return sorted(self._items, key=lambda p: p.get_price())
    
    def __getitem__(self, index):
        """Позволяет обращаться по индексу: catalog[0]"""
        return self._items[index]