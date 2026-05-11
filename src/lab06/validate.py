from datetime import *

def val_name(name):
        if not isinstance(name, str):
            raise TypeError(f'Неверный формат названия продукта')
        if name == '':
            raise ValueError('Название продукта не может быть пустым')
        return name
        
def val_price(price):
    if not isinstance(price, int):
        raise TypeError(f'Неверный формат цены')
    if price <= 0:
        raise ValueError(f'Цена должна быть положительной')
    return price

def val_quantity(quantity):
    if not isinstance(quantity, int):
        raise TypeError(f'Неверный формат количества продукта')
    if quantity < 0:
        raise ValueError(f'Количество продукта не может быть отрицательным')
    return quantity

def val_producer(producer):
    if not isinstance(producer, str):
        raise TypeError(f'Неверный формат поставщика')
    if len(producer.strip()) == 0:
        raise ValueError('Имя производителя не может быть пустым')
    return producer

def val_cost_price(cost_price):
    if not isinstance(cost_price, float):
        raise TypeError(f'Неверный формат себестоимости')
    if cost_price <= 0:
        raise ValueError(f'Себестоимость должна быть положительной')
    return cost_price  # Приватный атрибут


def val_id(id):
    if not isinstance(id, str):
        raise TypeError(f'Неверный формат id')
    if len(id) != 7 or id[0] != '#':
        raise ValueError(f'ID должен начинаться с # и содержать 7 символов')
    return id  # Защищенный атрибут

def val_description(description):
    if not isinstance(description, str):
        raise TypeError(f'Неверный формат описания')
    if len(description.strip()) == 0:
        raise ValueError('Описание продукта не может быть пустым')
    return description

def val_comments(comments):
    if not isinstance(comments, dict):
        raise TypeError(f'Комментарии должны быть словарем, а не {type(comments).__name__}')
    return comments #Проблема со ссылками? .copy()

def val_calories(calories):
    if not isinstance(calories, int):
        raise TypeError(f'Калории должны быть числом, а не {type(calories).__name__}')
    
def val_per(iod):
    if isinstance(iod, int):
        return iod
    else:
        raise TypeError('Период использования должен быть указан в формате ')

def val_months(m):
    if isinstance(m, int) and m >=0:
        return m
    else:
        raise TypeError(f'Неверный формат гарантийного срока')
    
def val_power(p):
    if isinstance(p, float) and p > 0.0:
        return p
    else:
        raise TypeError(f'ТЕМНЙ ПРИНЦ Ы А Ы А Ы А')

def val_loc(location):
    if isinstance(location, tuple) and len(location) == 2 and isinstance(location[0], float) and isinstance(location[1], float):
        return location
    else:
        raise TypeError(f'Дурашка ты')

def val_prop(proport):
    if isinstance(proport, int):
        return proport
    else:
        raise TypeError(f'Неверный формат размеров. Нужен int, а не {type(proport).__name__}')

def val_free(i):
    if i in [0, 1, True, False]:
        return i
    else:
        raise TypeError('Данный атрибут должен являться булевым значением')

