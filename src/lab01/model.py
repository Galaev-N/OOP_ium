class product:
    def __init__(self, name, price, quantity, producer, cost_price, id):
        if isinstance(name, str):
            self.name = name # название продукта
        else:
            raise 'Ошибка! Название продукта не может не содержать буквы'
        
        if isinstance(price, int):
            self.price = price # его цена
        else:
            raise 'Ошибка! Цена должна принимать целочисленное значение'
        
        if isinstance(quantity, int):
            self.quantity = quantity # кол-во в начличии
        else:
            raise 'Ошибка! Количество должно принимать целочисленное значение'
        
        if isinstance(producer, str):
            self.producer = producer # поставщик
        else:
            raise 'Ошибка! Имя поставщика не может не содержать буквы'
        
        if isinstance(cost_price, float):
            self.__cost_prise__ = cost_price 
        else:
            raise 'Ошибка! Неверный формат себестоимости'
        
        if isinstance(id, str) and id[0] == '#' and len(id) == 7:
            self._id = id
        else:
            raise 'Ошибка! Неверный формат индефикационного номера'
    
    def __str__(self):  # Краткая сводка 
        if self.quantity != 0:
            return f"{self.name} за {self.price}. Есть в наличии"
        else:
            return f"{self.name} за {self.price}. Товара нет в наличии :("
    
    def __repr__(self):  # Для отладки
        return f"product('{self.name}', '{self.price}', '{self.quantity}', '{self.producer}', '{self.__cost_prise__}', {self._id}')"
    
    def __eq__(self, another):
        return self.name == another.name

    @property
    def info(self):
        return f'Вот что мне удалось найти по запросу {self.name}:\n{self.name}, {self.price}, {self.quantity}, {self.producer}'
