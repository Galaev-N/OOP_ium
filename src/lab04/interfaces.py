from models import Estate, Techic, Food
from abc import ABC, abstractmethod
from validate import *

class ProductCatalog(ABC):

    def __init__(self, items=None):
        if items is None:
            self._items = []
        elif isinstance(items, list):
            flag = 1
            for i in items:
                if type(i) not in [Product, Estate, Techic, Food]:
                    flag = 0
            if flag:
                self._items = items
            else: raise ValueError('Неверное содержание списка!')
        else: raise TypeError('Ошибка! неверный формат каталога!')
        
    @property
    def items(self):
        return self._items

    def A(self, obj): # Add
        if type(obj) in [Product, Estate, Techic, Food]: self._items.append(obj)
        else: raise TypeError(f'Ошибка! {obj} не принадлежит классу Product')
        return f'Продукт {obj.name} был успешно добавлен!'

    def R(self, obj): # Remove
        if obj in self._items: self._items.remove(obj)
        else: raise ValueError(f'Такого продукта нет в каталоге')
        return f'Продукт {obj.name} был успешно Удален!'

    @abstractmethod
    def GAll(self): #Get All
        pass
    
    def FBI(self, id): # Find By Id
        for obj in self._items:
            if obj._id == id:
                return obj
    
    def __len__(self): # Это было проще, чем я думал
        return len(self._items)

    @abstractmethod
    def __iter__(self):
        # Возвращаем итератор от нашего списка
        return iter(self._items)
    
    def __getitem__(self, index): # Позволяет обращаться к элементам множества по индексу
        pass
    
    def RAI(self, index): # Remove At Index
        if index < 0 or index >= len(self._items):
            raise IndexError(f'Индекс {index} вне диапазона (0-{len(self._items)-1})')
        return self._items.pop(index)
    
    def SBP(self): # Sort By Price
         self._items = sorted(self._items, key=lambda x: x.price)
         return self._items
    
    def GAva(self): # Get Avalible
        Available_cat = ProductCatalog()
    
        for item in self._items:
            # Проверяем, что элемент - один из допустимых типов
            if type(item) in [Product, Estate, Techic, Food]:
            # Для Food и Techic проверяем quantity
                if hasattr(item, 'quantity') and not hasattr(item, 'free'):
                    if item.quantity != 0:
                        Available_cat.A(item)
                        # Для Estate проверяем free
                elif hasattr(item, 'free'):
                    if item.free == 1:
                        Available_cat.A(item)
            # Для обычного Product
                elif hasattr(item, 'quantity'):
                    if item.quantity != 0:
                        Available_cat.A(item)
    
        return Available_cat
    
    def GD(self): # Get Digital
        Digital_cat = ProductCatalog()
        for item in self._items:
            # Проверяем, что элемент - Product и есть в наличии
            if type(item).__name__ == 'Techic':
                Digital_cat.A(item)  # Добавляем в новую коллекцию
        return Digital_cat

    def GF(self):
        Food_cat = ProductCatalog()
        for item in self._items:
            # Проверяем, что элемент - Product и есть в наличии
            if type(item).__name__ == 'Food':
                Food_cat.A(item)  # Добавляем в новую коллекцию
        return Food_cat
    
    def GE(self):
        Estate_cat = ProductCatalog()
        for item in self._items:
            # Проверяем, что элемент - Product и есть в наличии
            if type(item).__name__ == 'Food':
                Estate_cat.A(item)  # Добавляем в новую коллекцию
        return Estate_cat

#-------------------------------------------#

#===========================================#
#===========================================#
#===========================================#

#-------------------------------------------#

class Product(ABC):
    def __init__(self, name, price, quantity, producer, cost_price, id, description, comments, mark=3.0, status=0):

        self.name = val_name(name)
        self.price = val_price(price)
        self.quantity = val_quantity(quantity)
        self.producer = val_producer(producer)
        self.__cost_price__ = val_cost_price(cost_price)  # приватный
        self._id = val_id(id)  # защищенный
        self.description = val_description(description)
        self.comments = val_comments(comments)
        self.mark = mark
        self._status = status # защищенный
    
            #========МАГИЧЕСКИЕ МЕТОДЫ========#

    def __str__(self):  # Краткая сводка 
        if self._status == 1:
            return 'На данный момент информация о товаре не доступна'
        else:

            if self.quantity != 0:
                return f"{self.name} за {self.price} рублей. Оценка - {self.mark} \nОписание:\n{self.description}\n Комментарии:\n {self.comments}\n Есть в наличии\n"
            else:
                return f"{self.name} за {self.price} рублей. Товара нет в наличии :("
    
    def __repr__(self):  # Для отладки
        return f"product({self.name}, {self.price}, {self.quantity}, {self.producer}, {self.__cost_price__}, {self._id}, {self.description}, {self.comments}, {self.mark}, {self._status})"
    
    def __eq__(self, another): # Сравниваение с другим экземляром
        if not isinstance(another, Product):
            return False
    
    # Сравниваем по названию
        return self.name == another.name
    
            #========PROPERTY МЕТОДЫ========#

    @property
    def info(self):
        if self._status == 1:
            return 'На данный момент информация о товаре не доступна'
        else:
            return f'Вот что мне удалось найти по запросу {self.name}:\n{self.name}, {self.price}, {self.quantity},\n{self.producer}, {self.description}, {self.comments}'
    
    @property
    def mark(self):
        return self._mark
    
    @property
    def cost_price(self):
        return self.__cost_price__
    
    @property
    def id(self):
        return self._id
    
    @property
    def _deficit(self):
        self._status = 1
        return f'... И к последним новостям экономики, в виду всеми известных событий начался дефицит продукта"{self.name}"'
    
    
    @mark.setter
    def mark(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f'Оценка должна быть числом')
        if value < 0.0 or value > 5.0:
            raise ValueError("Ошибка! Оценка должна быть числом от 0 до 5")
        self._mark = float(value)

            #========"БИЗНЕС" МЕТОДЫ========#

    def feadback(self, txt):
        self.comments[f'UnknowUser{len(self.comments)}'] = txt
        return 'Комментарий успешно добавлен!'

    def order(self, wallet):
        if self._status == 1:
            x = 1.22
        else:
            x = 1
        if wallet >= self.price*x and self.quantity > 0:
            self.quantity -=1
            return f'Отлично! Товар "{self.name}" успешно заказан!'
        elif wallet < self.price*x:
            return f'Отказ! Причина: недостаточно {self.price*x - wallet} на балансе'
        elif self.quantity == 0:
            return f'Отказ! Товара вида "{self.name}" нет в наличии'''
        
