class product:
    def __init__(self, name, price, quantity, producer, cost_price, id, description, comments):

        if isinstance(description, str):
            self.description = description # название продукта
        else:
            raise TypeError('Ошибка! Описание продукта должно содержать текст')
        
        if isinstance(comments, dict):
            self.comments = comments # название продукта
        else:
            raise TypeError('Ошибка! Не верный формат комментариев')

        if isinstance(name, str):
            self.name = name # название продукта
        else:
            raise TypeError('Ошибка! Название продукта не может не содержать буквы')
        
        if isinstance(price, int):
            self.price = price # его цена
        else:
            raise TypeError('Ошибка! Цена должна принимать целочисленное значение')
        
        if isinstance(quantity, int):
            self.quantity = quantity # кол-во в начличии
        else:
            raise TypeError('Ошибка! Количество должно принимать целочисленное значение')
        
        if isinstance(producer, str):
            self.producer = producer # поставщик
        else:
            raise TypeError('Ошибка! Имя поставщика не может не содержать буквы')
        
        if isinstance(cost_price, float):
            self.__cost_prise__ = cost_price 
        else:
            raise TypeError('Ошибка! Неверный формат себестоимости')
        
        if isinstance(id, str) and id[0] == '#' and len(id) == 7:
            self._id = id
        else:
            raise TypeError('Ошибка! Неверный формат индефикационного номера')
    
    def __str__(self):  # Краткая сводка 
        if self.quantity != 0:
            return f"{self.name} за {self.price} рублей. Есть в наличии"
        else:
            return f"{self.name} за {self.price} рублей. Товара нет в наличии :("
    
    def __repr__(self):  # Для отладки
        return f"product({self.name}, {self.price}, {self.quantity}, {self.producer}, {self.__cost_prise__}, {self._id}, {self.description}, {self.comments})"
    
    def __eq__(self, another):
        return self.name == another.name

    @property
    def info(self):
        return f'Вот что мне удалось найти по запросу {self.name}:\n{self.name}, {self.price}, {self.quantity},\n{self.producer}, {self.description}, {self.comments}'
    
    def feadback(self, txt):
        if self.comments != {}:
            n = self.comments.keys()[-1][-1] + 1
        else:
            n = 0
        self.comments[f'UnknowUser{n}'] = txt
        return 'Комментарий успешно добавлен!'

