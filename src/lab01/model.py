from validate import *
class Product:
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
        return self.__cost_price
    
    @property
    def id(self):
        return self._id
    
    @property
    def _deficit(self):
        self._status = 1
        return f'... И к последним новостям экономики, в виду всеми звестных событий начался дефицит продукта"{self.name}"'
    
    
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
            x = 1.2
        else:
            x = 1
        if wallet >= self.price*x and self.quantity > 0:
            self.quantity -=1
            return f'Отлично! Товар "{self.name}" успешно заказан!'
        elif wallet < self.price*x:
            return f'Отказ! Причина: недостаточно {self.price*x - wallet} на балансе'
        elif self.quantity == 0:
            return f'Отказ! Товара вида "{self.name}" нет в наличии'
