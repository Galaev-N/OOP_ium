import sys

sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab01')
from model import *

class ProductCatalog:

    #Проверка на флуд
    def __init__(self, items=None):
        if items is None:
            self._items = []
        elif isinstance(items, list):
            flag = 1
            for i in items:
                if type(i) != Product:
                    flag = 0
            if flag:
                self._items = items
            else: raise ValueError('Неверное содержание списка!')
        else: raise TypeError('Ошибка! неверный формат каталога!')
        

    def add(self, obj):
        if type(obj) == Product: self._items.append(obj)
        else: raise TypeError(f'Ошибка! {obj} не принадлежит классу Product')

    def remove(self, obj):
        if obj in self._items: self._items.remove(obj)
        else: raise ValueError(f'Такого продукта нет в каталоге')

    def get_all(self):
        return self._items
    
    def find_by_id(self, id):
        for obj in self._items:
            if obj._id == id:
                return obj
    
    def __len__(self): # Это было проще, чем я думал
        return len(self._items)

    def __iter__(self):
        # Возвращаем итератор от нашего списка
        return iter(self.items)

a = ProductCatalog()
print(len(a))