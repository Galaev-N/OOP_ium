from new_models import *

class ProductCatalog:

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

    def GAll(self): #Get All
        return f'Вот содержимое коллекции:\n{self._items}'
    
    def FBI(self, id): # Find By Id
        for obj in self._items:
            if obj._id == id:
                return obj
    
    def __len__(self): # Это было проще, чем я думал
        return len(self._items)

    def __iter__(self):
        # Возвращаем итератор от нашего списка
        return iter(self._items)
    
    def __getitem__(self, index): # Позволяет обращаться к элементам множества по индексу
        return self._items[index]
    
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
