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