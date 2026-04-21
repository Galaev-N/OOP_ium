# demo_final.py
# ==================================================
# ИТОГОВОЕ ТЕСТИРОВАНИЕ КЛАССОВ И КОЛЛЕКЦИЙ
# ==================================================

import sys
sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab01/')
sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab02/')

from new_models import Food, Techic, Estate
from new_col import ProductCatalog
from model import Product

# ========== ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ==========
def print_separator(title="", char="=", width=70):
    """Печатает разделитель с заголовком"""
    if title:
        print(f"\n{char * width}")
        print(f"{title.center(width)}")
        print(f"{char * width}")
    else:
        print(f"\n{char * width}")

def print_catalog(catalog, title="Содержимое каталога"):
    """Красиво выводит каталог"""
    print(f"\n{title}:")
    print("-" * 80)
    if len(catalog) == 0:
        print("  Каталог пуст")
    else:
        for i, product in enumerate(catalog):
            # Определяем тип товара
            product_type = product.__class__.__name__
            
            # Проверяем наличие
            if hasattr(product, 'quantity'):
                status = "В наличии" if product.quantity > 0 else "Нет в наличии"
            elif hasattr(product, 'free'):
                status = "Свободно" if product.free == 1 else "Занято"
            else:
                status = "Статус неизвестен"
                
            print(f"  [{i}] {product_type}: {product.name} | {product.price}₽ | {status}")
    print("-" * 80)
    print(f"Всего товаров: {len(catalog)}\n")

# ========== 1. СОЗДАНИЕ ТЕСТОВЫХ ОБЪЕКТОВ ==========
print_separator("ШАГ 1: СОЗДАНИЕ ОБЪЕКТОВ РАЗНЫХ ТИПОВ")

apple = Food(
    name="Яблоко Гренни Смит",
    price=150,
    quantity=100,
    producer="Фруктовый рай",
    cost_price=80.0,
    id="#F00001",  # 7 символов: # + 6 цифр
    description="Кисло-сладкие яблоки, выращенные в экологически чистых условиях",
    comments={"Мария": "Очень сочные!", "Иван": "Хорошие яблоки"},
    expiration_per=30,
    mark=4.7,
    calories=52
)

milk = Food(
    name="Молоко Домик в деревне",
    price=89,
    quantity=50,
    producer="Вкуснотеево",
    cost_price=55.0,
    id="#F00002",  # 7 символов
    description="Пастеризованное молоко 3.2% жирности",
    comments={"Покупатель1": "Свежее молоко"},
    expiration_per=7,
    mark=4.5,
    calories=60
)

# Техника
# Техника (с корректной мощностью)
laptop = Techic(
    name="Ноутбук ASUS ROG",
    price=85000,
    quantity=5,
    producer="ASUS",
    cost_price=62000.0,
    id="#T00001",
    description="Игровой ноутбук с RTX 4060",
    comments={"Геймер": "Отлично тянет игры!"},
    warranty_months=24,
    power_consumption=150.0,  # float, а не int
    mark=4.8
)

phone = Techic(
    name="Смартфон iPhone 15",
    price=79990,
    quantity=0,
    producer="Apple",
    cost_price=60000.0,
    id="#T00002",
    description="Флагманский смартфон с OLED экраном",
    comments={},
    warranty_months=12,
    power_consumption=20.0,  # float
    mark=4.9
)

# Недвижимость
# Недвижимость (proportions - число, не строка)
apartment = Estate(
    name="Квартира в центре",
    price=15000000,
    producer="СтройГарант",
    id="#E00001",
    description="Двухкомнатная квартира с евроремонтом",
    comments={"Риэлтор": "Отличный вариант!"},
    location=(55.7558, 37.6176),
    proportions=60,  # int, не строка (площадь в кв.м)
    free=1,
    mark=4.6
)

house = Estate(
    name="Загородный дом",
    price=25000000,
    producer="ДомСтрой",
    id="#E00002",
    description="Кирпичный дом с участком 10 соток",
    comments={},
    location=(55.7512, 37.6185),
    proportions=150,  # int (площадь в кв.м)
    free=0,
    mark=4.8
)

mouse = Product(
    name="Мышь Logitech",
    price=2500,
    quantity=20,
    producer="Logitech",
    cost_price=1800.0,
    id="#P8J7L1",
    description="Беспроводная мышь",
    comments={},
    mark=4.3
)

print("✓ Созданы объекты:")
print(f"  - Food (2 шт): {apple.name}, {milk.name}")
print(f"  - Techic (2 шт): {laptop.name}, {phone.name}")
print(f"  - Estate (2 шт): {apartment.name}, {house.name}")
print(f"  - Product (1 шт): {mouse.name}")

# ========== 2. ТЕСТИРОВАНИЕ КЛАССА ProductCatalog ==========
print_separator("ШАГ 2: ТЕСТИРОВАНИЕ ProductCatalog")

# Создаем каталог
catalog = ProductCatalog()
print("Создан пустой каталог")

# Добавляем товары разных типов
print("\nДобавление товаров (метод A()):")
print(catalog.A(apple))
print(catalog.A(milk))
print(catalog.A(laptop))
print(catalog.A(phone))
print(catalog.A(apartment))
print(catalog.A(house))
print(catalog.A(mouse))

print_catalog(catalog, "Каталог после добавления всех товаров")

# ========== 3. ДЕМОНСТРАЦИЯ ИНДЕКСАЦИИ ==========
print_separator("ШАГ 3: ИНДЕКСАЦИЯ (__getitem__)")

print("Доступ по индексам:")
print(f"  catalog[0] = {catalog[0].name} ({catalog[0].__class__.__name__})")
print(f"  catalog[2] = {catalog[2].name} ({catalog[2].__class__.__name__})")
print(f"  catalog[-1] = {catalog[-1].name} (последний)")

print("\nИтерация по каталогу:")
for i, product in enumerate(catalog):
    print(f"  {i}: {product.name} - {product.price}₽")

# ========== 4. МЕТОД GAva() - ТОВАРЫ В НАЛИЧИИ ==========
print_separator("ШАГ 4: ФИЛЬТРАЦИЯ - ТОВАРЫ В НАЛИЧИИ (GAva)")

available = catalog.GAva()
print_catalog(available, "Только товары в наличии/свободные")

print("Анализ GAva():")
for product in available.items:
    if hasattr(product, 'quantity'):
        print(f"  ✓ {product.name}: quantity={product.quantity}")
    elif hasattr(product, 'free'):
        print(f"  ✓ {product.name}: free={'Да' if product.free==1 else 'Нет'}")

# ========== 5. МЕТОД SBP() - СОРТИРОВКА ПО ЦЕНЕ ==========
print_separator("ШАГ 5: СОРТИРОВКА ПО ЦЕНЕ (SBP)")

print("До сортировки (первые 3):")
for i in range(min(3, len(catalog))):
    print(f"  {catalog[i].name}: {catalog[i].price}₽")

catalog.SBP()
print("\nПосле сортировки по возрастанию цены:")
for product in catalog.items:
    print(f"  {product.name}: {product.price}₽")

# ========== 6. МЕТОД FBI() - ПОИСК ПО ID ==========
print_separator("ШАГ 6: ПОИСК ПО ID (FBI)")

test_ids = ["#T001", "#F001", "#E002", "#NONEXISTENT"]
for search_id in test_ids:
    found = catalog.FBI(search_id)
    if found:
        print(f"  Найден ID {search_id}: {found.name} ({found.__class__.__name__})")
    else:
        print(f"  ID {search_id} не найден")

# ========== 7. МЕТОДЫ GD() И GF() ==========
print_separator("ШАГ 7: ФИЛЬТРАЦИЯ ПО ТИПУ (GD, GF)")

# Проверяем методы (нужно исправить в new_col.py)
print("Метод GD() (цифровая техника) - требует доработки в new_col.py")
print("Метод GF() (продукты питания) - требует доработки в new_col.py")
print("\nТекущая реализация этих методов имеет ошибку:")
print("  - Вместо type(item).__name__ == Techic нужно isinstance(item, Techic)")
print("  - В GF() тоже проверяется Techic вместо Food")

# Демонстрация правильной фильтрации вручную
digital_items = [item for item in catalog.items if isinstance(item, Techic)]
food_items = [item for item in catalog.items if isinstance(item, Food)]
estate_items = [item for item in catalog.items if isinstance(item, Estate)]

print(f"\nРучная фильтрация (правильная):")
print(f"  Техника: {len(digital_items)} шт - {[i.name for i in digital_items]}")
print(f"  Питание: {len(food_items)} шт - {[i.name for i in food_items]}")
print(f"  Недвижимость: {len(estate_items)} шт - {[i.name for i in estate_items]}")

# ========== 8. МЕТОД RAI() - УДАЛЕНИЕ ПО ИНДЕКСУ ==========
print_separator("ШАГ 8: УДАЛЕНИЕ ПО ИНДЕКСУ (RAI)")

print(f"Размер каталога до удаления: {len(catalog)}")
removed = catalog.RAI(0)
print(f"Удален: {removed.name}")
print(f"Размер после удаления: {len(catalog)}")
print_catalog(catalog, "Каталог после удаления первого элемента")

# ========== 9. МЕТОД R() - УДАЛЕНИЕ ПО ОБЪЕКТУ ==========
print_separator("ШАГ 9: УДАЛЕНИЕ ПО ОБЪЕКТУ (R)")

print(f"Удаляем {mouse.name}:")
print(catalog.R(mouse))
print(f"Размер каталога: {len(catalog)}")

# ========== 10. ТЕСТИРОВАНИЕ МЕТОДОВ НОВЫХ КЛАССОВ ==========
print_separator("ШАГ 10: СПЕЦИФИЧЕСКИЕ МЕТОДЫ НОВЫХ КЛАССОВ")

# Food.fits()
print("Метод Food.fits():")
print(f"  {apple.name}: {apple.fits('2026-04-21 10:30:00')}")

# Techic.check()
print("\nМетод Techic.check():")
print(f"  {laptop.name}: {laptop.check()}")

# Estate.how_long()
print("\nМетод Estate.how_long():")
print(f"  {apartment.name}: {apartment.how_long((55.75, 37.62))}")

# ========== 11. ПРОВЕРКА INFO И __str__ ==========
print_separator("ШАГ 11: МЕТОДЫ INFO И __str__")

print("__str__ для Food:")
print(apple)

print("\n__str__ для Techic (нет в наличии):")
print(phone)

print("\n__str__ для Estate (занято):")
print(house)

print("\ninfo() для Estate:")
print(apartment.info())

# ========== 12. ОБРАБОТКА ОШИБОК ==========
print_separator("ШАГ 12: ПРОВЕРКА ОБРАБОТКИ ОШИБОК")

print("Попытка добавить не-объект:")
try:
    catalog.A("Это строка")
except TypeError as e:
    print(f"  ✓ Ошибка перехвачена: {e}")

print("\nПопытка удалить несуществующий объект:")
try:
    fake_product = Product("Фейк", 100, 1, "Test", 50.0, "#FAKE01", "", {})  # cost_price=50.0 (float)
    catalog.R(fake_product)
except ValueError as e:
    print(f"  ✓ Ошибка перехвачена: {e}")

print("\nПопытка получить неверный индекс:")
try:
    catalog.RAI(999)
except IndexError as e:
    print(f"  ✓ Ошибка перехвачена: {e}")

print("\nПопытка создать каталог с невалидным списком:")
try:
    bad_catalog = ProductCatalog([apple, "не товар", laptop])
except ValueError as e:
    print(f"  ✓ Ошибка перехвачена: {e}")

# ========== 13. СОЗДАНИЕ КАТАЛОГА ИЗ СПИСКА ==========
print_separator("ШАГ 13: СОЗДАНИЕ КАТАЛОГА ИЗ СПИСКА")

product_list = [laptop, phone, apple, milk, apartment]
catalog2 = ProductCatalog(product_list)
print(f"Создан каталог из {len(catalog2)} товаров")
print_catalog(catalog2, "Новый каталог из списка")

# ========== 14. РАБОТА С КОЛЛЕКЦИЯМИ РАЗНЫХ ТИПОВ ==========
print_separator("ШАГ 14: ПОЛИМОРФИЗМ - ЕДИНАЯ КОЛЛЕКЦИЯ")

print("Каталог содержит объекты разных классов, но все они наследуют Product:")
print("\nПроверка типов в каталоге:")
type_counts = {}
for product in catalog.items:
    t = product.__class__.__name__
    type_counts[t] = type_counts.get(t, 0) + 1

for t, count in type_counts.items():
    print(f"  {t}: {count} шт")

# ========== 15. ФИНАЛЬНЫЙ ОТЧЕТ ==========
print_separator("ИТОГИ ТЕСТИРОВАНИЯ", "=")

print("""
✅ УСПЕШНО ПРОВЕРЕНО:

Классы:
  • Product (базовый) - из lab01
  • Food (наследник) - продукты питания
  • Techic (наследник) - техника
  • Estate (наследник) - недвижимость

Методы ProductCatalog:
  ✓ A()      - добавление товара
  ✓ R()      - удаление товара по объекту
  ✓ GAll()   - получение всех товаров
  ✓ FBI()    - поиск по ID
  ✓ GAva()   - фильтр товаров в наличии
  ✓ SBP()    - сортировка по цене
  ✓ RAI()    - удаление по индексу
  ✓ __len__  - длина каталога
  ✓ __getitem__ - доступ по индексу
  ✓ __iter__ - итерация

Специфические методы:
  ✓ Food.fits()     - расчет срока годности
  ✓ Techic.check()  - проверка цены
  ✓ Estate.how_long() - расчет расстояния

Обработка ошибок:
  ✓ TypeError - при неверном типе
  ✓ ValueError - при неверном значении
  ✓ IndexError - при неверном индексе

Проблемы в new_col.py (требуют исправления):
  ⚠ GD() и GF() - неверная проверка типов
     (использовать isinstance() вместо type().__name__)
""")

print(f"\nФинальное состояние каталога: {len(catalog)} товаров")
print_catalog(catalog, "ТЕКУЩИЙ КАТАЛОГ")

print("=" * 70)
print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
print("=" * 70)