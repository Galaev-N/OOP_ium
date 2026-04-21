import sys
from validate import *
from datetime import *
import random
sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab01/')

from model import Product

class Food(Product):
    def __init__(self, name, price, quantity, producer, cost_price, id,
                  description, comments, expiration_per, mark=3.0, status=0, calories=0):
        super().__init__(
            name=name,           # название
            price=price,         # цена
            quantity=quantity,          # количество (для недвижимости обычно 1 объект)
            producer=producer,   # производитель/застройщик
            cost_price=cost_price,  # себестоимость (можно рассчитать или передать отдельно)
            id=id,               # идентификатор
            description=description,  # описание
            comments=comments,   # комментарии
            )
        
        self.calories = val_calories(calories)
        self.expiration_per = val_per(expiration_per)
    
    def __str__(self):
        if self._status == 1:
            return 'На данный момент информация о продукте не доступна'
        else:
            if self.quantity != 0:
                return f"{self.name} за {self.price} рублей, срок годности: {self.expiration_per} дней.\nКалории: {self.calories}\nОценка продукта - {self.mark} \nОписание:\n{self.description}\nКомментарии:\n{self.comments}\nЕсть в наличии\n"
            else:
                return f"{self.name} за {self.price} рублей. Продукта нет в наличии :("
    
    def fits(self, our_day):
        try:
            purchase_date = datetime.strptime(our_day, '%Y-%m-%d %H:%M:%S')
            
            expiration_date = purchase_date + timedelta(self.expiration_per)
            
            return f'Купленный {our_day} продукт может быть употреблен до {expiration_date}'
        except:
            return f'Неверный формат даты'
            
    def info(self):
        if self._status == 1:
            return 'Просим прощения. Информация о продукте отсутствует'
        else:
            return f'Продукт питания "{self.name}":\n{self.calories}, {self.expiration_date} {self.price}, {self.quantity},\n{self.producer}, {self.description}, {self.comments}'


class Techic(Product):
    def __init__(self, name, price, quantity, producer, cost_price, id,
                  description, comments, warranty_months, power_consumption, mark=3.0, status=0):
        super().__init__(
            name=name,          
            price=price,         
            quantity=quantity,        
            producer=producer,   
            cost_price=cost_price,
            id=id,               
            description=description,  
            comments=comments,   
            mark=mark            
        )
        self.warranty_months = val_months(warranty_months)
        self.power_consumption = val_power(power_consumption)
    
    def __str__(self):
        if self._status == 1:
            return 'На данный момент информация о данной технике не доступна'
        else:
            if self.quantity != 0:
                return f"{self.name} за {self.price} рублей, с гарантийным сроком: {self.expiration_date}\nПотреблением энергии: {self.calories}\nОценка продукта- {self.mark} \nОписание:\n{self.description}\n Комментарии:\n {self.comments}\n Есть в наличии\n"
            else:
                return f"{self.name} за {self.price} рублей. Нет в наличии :("

    def info(self):
        if self._status == 1:
            return 'Просим прощения. Информация о данной технике отсутствует'
        else:
            return f'{self.name}":\n{self.warranty_months}, {self.power_consumption} {self.price}, {self.quantity},\n Производитель:{self.producer}\n {self.description}, {self.comments}'

    def check(self):
        a = random.randint(1, 3)
        if a == 1:
            return f'Вам удалось найти {self.name} дешвле, чем в объявдлении, нахр капец блин ваще'
        
        elif a == 2:
            return f'Кажется предложение за {self.price} действительно самое выгодное!'
        
        else:
            return f'Знайте-ка, РКН решил забанить нашу площадку из-за слишком выокой активности. Спасибо вам!'

class Estate(Product):
    def __init__(self, name, price, producer, id, description, comments, location, proportions, free=1, mark=3.0, status=0):
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
        self.proportions = val_prop(proportions)
        self.free = free
    def __str__(self):
        if self._status == 1:
            return 'На данный момент доступ к информации закрыт'
        else:
            if self.free == 1:
                return f"{self.name} за {self.price} рублей, Размеры: {self.proportions}\nНаходится по адресу: {self.location}\nОценка - {self.mark} \nОписание:\n{self.description}\n Комментарии:\n {self.comments}\n Свободно"
            
            else:
                return f"{self.name} за {self.price} рублей, Размеры: {self.proportions}\nНаходится по адресу: {self.location}\nОценка - {self.mark} \nОписание:\n{self.description}\n Комментарии:\n {self.comments}\n Занятно\n"
    def info(self):
        if self._status == 1:
            return 'Просим прощения. Информация о продукте отсутствует'
        elif self.free:
            return f'{self.name}:\n Расположение - {self.location}\n{self.proportions} {self.price}\n{self.producer}\n  {self.description}, {self.comments}'
        else:
            return f'{self.name}:\n Расположение - {self.location}\n{self.proportions} {self.price}, В данный момент занято\n{self.producer}\n  {self.description}, {self.comments}'
        
    def how_long(self, yo_loc):
        try:
            res = ((yo_loc[0] - self.location[0])**2 + (yo_loc[1] - self.location[1])**2)**0,5
            return f'Расстояние до места - {res} км.'
        except:
            return 'Неверный формат Местоположения'


A = Food('a', 100, 1000, 'aaa', 10.0, '#M67890', 'sssss', {}, 29)
print(type(type(A).__name__))
