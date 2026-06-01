from __future__ import annotations

import sys
from pathlib import Path
from typing import cast

CURRENT_DIR = Path(__file__).resolve().parent
LAB05_DIR = CURRENT_DIR.parent / "lab05"
if str(LAB05_DIR) not in sys.path:
    sys.path.insert(0, str(LAB05_DIR))

from new_models import Product, Food, Technic, Estate
from .container import TypedCollection, Displayable, Scorable, D, S


# В прошлых лабах у классов нет display() и score().
# Для Protocol наследование не нужно, достаточно наличия методов.
# Поэтому добавляем методы к уже существующим классам, не переписывая lab01-lab05.
def product_display(self: Product) -> str:
    return f"{self.__class__.__name__}: {self.name} | цена: {self.price} | оценка: {self.mark}"


def product_score(self: Product) -> float:
    return float(self.mark)


for cls in (Product, Food, Technic, Estate):
    cls.display = product_display
    cls.score = product_score


def print_collection(title: str, collection: TypedCollection[Product]) -> None:
    print(f"\n{title}")
    print("-" * 70)
    for index, item in enumerate(collection):
        print(f"[{index}] {item.name} | {item.__class__.__name__} | {item.price} руб.")
    print(f"Всего объектов: {len(collection)}")


print("=" * 70)
print("ЛАБОРАТОРНАЯ 6: GENERIC, TYPEVAR, PROTOCOL")
print("=" * 70)

# Создание объектов из прошлых лабораторных
laptop = Product(
    "Ноутбук", 150000, 5, "Asus", 100000.0, "#A00001",
    "Мощный игровой ноутбук", {"user1": "Отлично!"}, mark=4.8
)

book = Product(
    "Книга", 500, 50, "Издательство", 300.0, "#A00005",
    "Интересная книга", {"user4": "Шедевр!"}, mark=4.9
)

apples = Food(
    "Яблоки", 150, 100, "Фруктовая компания", 80.0, "#F00002",
    "Свежие красные яблоки", {"user2": "Вкусно!"}, expiration_per=14,
    mark=4.5, calories=52
)

tv = Technic(
    "Телевизор", 50000, 3, "Samsung", 35000.0, "#T00003",
    "4K Ultra HD", {"user3": "Хороший"}, warranty_months=24,
    power_consumption=120.0, mark=4.2
)

flat = Estate(
    "Квартира", 5000000, "Застройщик", "#E00004",
    "Просторная квартира в центре", {}, location=(55.75, 37.62),
    proportions=75, free=1, mark=4.9
)

# ============================================================
# СЦЕНАРИЙ 1. TypedCollection[Product] и проверка типа
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 1: типизированная коллекция Product")
print("=" * 70)

products: TypedCollection[Product] = TypedCollection(item_type=Product)
products.add(laptop)
products.add(book)
products.add(apples)
products.add(tv)
products.add(flat)

print_collection("Коллекция после добавления объектов:", products)

print("\nПроверка валидации типа при добавлении:")
try:
    products.add("это строка, а не товар")  # type: ignore[arg-type]
except TypeError as error:
    print(f"Ошибка поймана: {error}")

print("\nПолучение всех элементов через get_all():")
for item in products.get_all():
    print(f"- {item.name}")

# ============================================================
# СЦЕНАРИЙ 2. find()
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 2: find()")
print("=" * 70)

found = products.find(lambda item: item.name == "Телевизор")
print(f"Найденный элемент: {found.name if found else None}")

not_found = products.find(lambda item: item.name == "Пылесос")
print(f"Несуществующий элемент: {not_found}")

# ============================================================
# СЦЕНАРИЙ 3. filter()
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 3: filter()")
print("=" * 70)

expensive = products.filter(lambda item: item.price > 1000)
print("Товары дороже 1000 рублей:")
for item in expensive:
    print(f"- {item.name}: {item.price} руб.")

high_mark = products.filter(lambda item: item.mark >= 4.8)
print("\nТовары с оценкой >= 4.8:")
for item in high_mark:
    print(f"- {item.name}: {item.mark}")

# ============================================================
# СЦЕНАРИЙ 4. map() и смена типа результата
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 4: map() меняет тип результата")
print("=" * 70)

names: list[str] = products.map(lambda item: item.name)
prices: list[int] = products.map(lambda item: item.price)
marks: list[float] = products.map(lambda item: item.mark)

print(f"list[str]  names  = {names}")
print(f"list[int]  prices = {prices}")
print(f"list[float] marks = {marks}")

# ============================================================
# СЦЕНАРИЙ 5. Protocol Displayable
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 5: Protocol Displayable")
print("=" * 70)

display_items: TypedCollection[D] = TypedCollection(item_type=Displayable)
display_items.add(cast(D, laptop))
display_items.add(cast(D, apples))
display_items.add(cast(D, tv))
display_items.add(cast(D, flat))

print("Объекты разных классов подходят под Displayable без наследования от Protocol:")
for item in display_items:
    print(f"- {item.display()}")

# ============================================================
# СЦЕНАРИЙ 6. Protocol Scorable
# ============================================================
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 6: Protocol Scorable")
print("=" * 70)

score_items: TypedCollection[S] = TypedCollection(item_type=Scorable)
score_items.add(cast(S, book))
score_items.add(cast(S, apples))
score_items.add(cast(S, flat))

print("Один и тот же TypedCollection работает с другим ограничением:")
for item in score_items:
    print(f"- {item.display()} | score = {item.score()}")

average_score = sum(score_items.map(lambda item: item.score())) / len(score_items)
print(f"\nСредняя оценка: {average_score:.2f}")

print("\n" + "=" * 70)
print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
print("=" * 70)
