# demo.py

from childrens import Food, Techic, Estate, ProductCatalog
from N_inter import Product, Catalog, Comparable

# ============ УНИВЕРСАЛЬНЫЕ ФУНКЦИИ ============
def print_all_products(products):
    for product in products:
        if isinstance(product, Product):
            print(f"  • {product}")


def find_cheapest(products):
    if not products:
        return None
    cheapest = products[0]
    for product in products[1:]:
        if product.compare_to(cheapest) < 0:
            cheapest = product
    return cheapest


# ============ СОЗДАНИЕ ТОВАРОВ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 1: СОЗДАНИЕ ТОВАРОВ")
print("=" * 70)

# Food
apple = Food(
    name="Яблоко",
    price=50,
    quantity=100,
    producer="ФруктСад",
    cost_price=30.0,
    id="#F00001",           # # + 6 символов = 7 ✅
    description="Сочные красные яблоки",
    comments={},
    expiration_days=14,
    calories=52,
    mark=4.5,
    status=0
)

banana = Food(
    name="Банан",
    price=80,
    quantity=50,
    producer="Тропик",
    cost_price=40.0,
    id="#F00002",           # # + 6 символов = 7 ✅
    description="Сладкий спелый банан",
    comments={},
    expiration_days=7,
    calories=95,
    mark=4.2,
    status=0
)

# Techic
laptop = Techic(
    name="MacBook Pro",
    price=120000,
    quantity=5,
    producer="Apple",
    cost_price=90000.0,
    id="#T00001",           # # + 6 символов = 7 ✅
    description="Мощный ноутбук для работы",
    comments={},
    warranty_months=24,
    power_consumption=60.0,
    mark=4.8,
    status=0
)

phone = Techic(
    name="iPhone 15",
    price=80000,
    quantity=10,
    producer="Apple",
    cost_price=60000.0,
    id="#T00002",           # # + 6 символов = 7 ✅
    description="Смартфон с отличной камерой",
    comments={},
    warranty_months=12,
    power_consumption=5.0,
    mark=4.7,
    status=0
)

# Estate
apartment = Estate(
    name="Квартира на Ленина",
    price=5000000,
    producer="СтройТрест",
    id="#E00001",           # # + 6 символов = 7 ✅
    description="Просторная квартира в центре",
    comments={},
    location=(55.75, 37.62),
    area=65,
    mark=4.9,
    free=1,
    status=0
)

house = Estate(
    name="Загородный дом",
    price=8000000,
    producer="ЗагородСтрой",
    id="#E00002",           # # + 6 символов = 7 ✅
    description="Уютный дом с садом",
    comments={},
    location=(55.80, 37.70),
    area=120,
    mark=4.7,
    free=1,
    status=0
)

# Фиктивный товар для теста
dummy = Food(
    name="Фикция",
    price=1,
    quantity=0,
    producer="Тест",
    cost_price=1.0,
    id="#X99999",           # # + 6 символов = 7 ✅ (#X99999)
    description="Тестовый товар",
    comments={},
    expiration_days=1
)

print("✓ Все товары созданы")


# ============ СЦЕНАРИЙ 2: МЕТОДЫ PRODUCT ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 2: МЕТОДЫ ИНТЕРФЕЙСА PRODUCT")
print("=" * 70)

print("\n> get_price():")
print(f"  Яблоко: {apple.get_price()} руб.")
print(f"  Ноутбук: {laptop.get_price()} руб.")
print(f"  Квартира: {apartment.get_price()} руб.")

print("\n> is_available():")
print(f"  Яблоко: {'В наличии' if apple.is_available() else 'Нет'}")
print(f"  Ноутбук: {'В наличии' if laptop.is_available() else 'Нет'}")
print(f"  Квартира: {'Свободна' if apartment.is_available() else 'Занята'}")

print("\n> order():")
print(f"  {apple.order(30)}")
print(f"  {apple.order(100)}")
print(f"  {laptop.order(100000)}")
print(f"  {apartment.order(6000000)}")

print("\n> __str__():")
print(f"  {apple}")
print(f"  {laptop}")


# ============ СЦЕНАРИЙ 3: КАТАЛОГ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 3: РАБОТА С КАТАЛОГОМ")
print("=" * 70)

catalog = ProductCatalog()
print(f"\n> add():")
print(f"  {catalog.add(apple)}")
print(f"  {catalog.add(banana)}")
print(f"  {catalog.add(laptop)}")
print(f"  {catalog.add(phone)}")
print(f"  {catalog.add(apartment)}")
print(f"  {catalog.add(house)}")
print(f"  Размер: {len(catalog)}")

print(f"\n> get_all():")
for p in catalog.get_all():
    print(f"    • {p.get_name()} - {p.get_price()} руб.")

print(f"\n> find_by_id('#T00001'):")
found = catalog.find_by_id("#T00001")
print(f"    Найден: {found.get_name() if found else 'None'}")

print(f"\n> get_available():")
for p in catalog.get_available():
    print(f"    • {p.get_name()}")

print(f"\n> sort_by_price():")
for p in catalog.sort_by_price():
    print(f"    • {p.get_name()}: {p.get_price()} руб.")

print(f"\n> remove(banana):")
print(f"  {catalog.remove(banana)}")
print(f"  Размер после удаления: {len(catalog)}")

print(f"\n> __iter__():")
for i, p in enumerate(catalog):
    print(f"    {i+1}. {p.get_name()}")

print(f"\n> __getitem__(2):")
print(f"    {catalog[2].get_name()}")


# ============ СЦЕНАРИЙ 4: ПОЛИМОРФИЗМ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 4: ПОЛИМОРФИЗМ")
print("=" * 70)

products_list = [apple, laptop, phone, apartment]

print("\n> print_all_products():")
print_all_products(products_list)

print("\n> find_cheapest():")
cheapest = find_cheapest(products_list)
if cheapest:
    print(f"    {cheapest.get_name()} - {cheapest.get_price()} руб.")


# ============ СЦЕНАРИЙ 5: isinstance ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 5: ПРОВЕРКА isinstance")
print("=" * 70)

print(f"\n  apple is Product: {isinstance(apple, Product)}")
print(f"  laptop is Product: {isinstance(laptop, Product)}")
print(f"  laptop is Comparable: {isinstance(laptop, Comparable)}")
print(f"  catalog is Catalog: {isinstance(catalog, Catalog)}")
print(f"  'str' is Product: {isinstance('str', Product)}")


# ============ СПЕЦИФИЧНЫЕ МЕТОДЫ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 6: СПЕЦИФИЧНЫЕ МЕТОДЫ")
print("=" * 70)

print(f"\n  apple.check_expiration(): {apple.check_expiration()}")
print(f"  laptop.check_price_online(): {laptop.check_price_online()}")


# ============ ИТОГ ============
print("\n" + "=" * 70)
print("ИТОГ")
print("=" * 70)
print("✓ 2 интерфейса: Product, Catalog")
print("✓ Дополнительный интерфейс: Comparable")
print("✓ isinstance для интерфейсов")
print("✓ super() в классах")
print("✓ Полиморфизм через интерфейс")
print("✓ Разная реализация методов")
print("✓ Валидация данных")
print("=" * 70)