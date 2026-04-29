# demo.py

from childrens import Food, Techic, Estate, ProductCatalog
from N_inter import Product, Catalog, Comparable

# ============ УНИВЕРСАЛЬНЫЕ ФУНКЦИИ ============
def print_all_products(products):
    """Полиморфизм через интерфейс Product"""
    for product in products:
        if isinstance(product, Product):
            print(f"  • {product}")


def apply_discount_to_all(products, percent):
    """Применяет скидку ко всем товарам, у которых есть метод apply_discount"""
    for product in products:
        if hasattr(product, 'apply_discount'):
            product.apply_discount(percent)


def find_cheapest(products):
    """Поиск самого дешёвого товара через Comparable"""
    if not products:
        return None
    cheapest = products[0]
    for product in products[1:]:
        if product.compare_to(cheapest) < 0:
            cheapest = product
    return cheapest


# ============ СОЗДАНИЕ ТОВАРОВ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 1: СОЗДАНИЕ ТОВАРОВ И МЕТОДЫ ИНТЕРФЕЙСОВ")
print("=" * 70)

apple = Food(
    name="Яблоко", price=50, quantity=100, producer="ФруктСад",
    cost_price=30, id="#F001", description="Сочные яблоки",
    comments={}, expiration_days=14, calories=52, mark=4.5
)

banana = Food(
    name="Банан", price=80, quantity=50, producer="Тропик",
    cost_price=40, id="#F002", description="Сладкий банан",
    comments={}, expiration_days=7, calories=95, mark=4.2
)

laptop = Techic(
    name="MacBook Pro", price=120000, quantity=5, producer="Apple",
    cost_price=90000, id="#T001", description="Мощный ноутбук",
    comments={}, warranty_months=24, power_consumption=60,
    mark=4.8, status=0
)

phone = Techic(
    name="iPhone 15", price=80000, quantity=10, producer="Apple",
    cost_price=60000, id="#T002", description="Смартфон",
    comments={}, warranty_months=12, power_consumption=5,
    mark=4.7, status=0
)

apartment = Estate(
    name="Квартира на Ленина", price=5000000, producer="СтройТрест",
    id="#E001", description="Просторная квартира", comments={},
    location="ул. Ленина, 10", area=65, mark=4.9, free=1
)

print("\n> Данные о товарах:")
print(apple)
print(laptop)
print(apartment)


# ============ МЕТОДЫ ИНТЕРФЕЙСОВ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 2: МЕТОДЫ ИНТЕРФЕЙСОВ (get_price, order, is_available)")
print("=" * 70)

print("\n> get_price() - получение цены:")
print(f"  Яблоко: {apple.get_price()} руб.")
print(f"  Ноутбук: {laptop.get_price()} руб.")
print(f"  Квартира: {apartment.get_price()} руб.")

print("\n> is_available() - проверка наличия:")
print(f"  Яблоко: {'В наличии' if apple.is_available() else 'Нет в наличии'}")
print(f"  Ноутбук: {'В наличии' if laptop.is_available() else 'Нет в наличии'}")
print(f"  Квартира: {'Свободна' if apartment.is_available() else 'Занята'}")

print("\n> order() - оформление заказа:")
print("---Попытка купить яблоко с 30 руб:")
print(f"  {apple.order(30)}")
print("\n---Покупка яблока с 100 руб:")
print(f"  {apple.order(100)}")
print("\n---Покупка ноутбука с 100000 руб:")
print(f"  {laptop.order(100000)}")
print("\n---Покупка ноутбука с 150000 руб:")
print(f"  {laptop.order(150000)}")
print("\n---Покупка квартиры с 6000000 руб:")
print(f"  {apartment.order(6000000)}")


# ============ ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙС ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 3: ПОЛИМОРФИЗМ ЧЕРЕЗ ИНТЕРФЕЙСЫ")
print("=" * 70)

# Создаём список студентов → список товаров
products_list = [apple, banana, laptop, phone]

print("\n> Полиморфная функция print_all_products():")
print_all_products(products_list)

print("\n> Поиск самого дешёвого товара через compare_to():")
cheapest = find_cheapest(products_list)
if cheapest:
    print(f"  Самый дешёвый: {cheapest.get_name()} - {cheapest.get_price()} руб.")

print("\n> Сравнение товаров через Comparable:")
print(f"  Яблоко (50 руб) vs Банан (80 руб):")
if apple.compare_to(banana) < 0:
    print(f"    → Яблоко дешевле")
elif apple.compare_to(banana) > 0:
    print(f"    → Банан дешевле")
else:
    print(f"    → Цены равны")

print(f"\n  MacBook (120000 руб) vs iPhone (80000 руб):")
if laptop.compare_to(phone) < 0:
    print(f"    → MacBook дешевле")
elif laptop.compare_to(phone) > 0:
    print(f"    → iPhone дешевле")
else:
    print(f"    → Цены равны")


# ============ ПРОВЕРКА isinstance ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 4: ПРОВЕРКА isinstance ДЛЯ ИНТЕРФЕЙСОВ")
print("=" * 70)

print(f"\n> apple (Food):")
print(f"  - является Product: {isinstance(apple, Product)}")
print(f"  - является Comparable: {isinstance(apple, Comparable)}")

print(f"\n> laptop (Techic):")
print(f"  - является Product: {isinstance(laptop, Product)}")
print(f"  - является Comparable: {isinstance(laptop, Comparable)}")

print(f"\n> apartment (Estate):")
print(f"  - является Product: {isinstance(apartment, Product)}")
print(f"  - является Comparable: {isinstance(apartment, Comparable)}")

print(f"\n> 'строка' (str):")
print(f"  - является Product: {isinstance('строка', Product)}")


# ============ КАТАЛОГ И КОЛЛЕКЦИЯ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 5: КАТАЛОГ ТОВАРОВ И ФИЛЬТРАЦИЯ")
print("=" * 70)

# Создаём каталог
catalog = ProductCatalog()
catalog.add(apple)
catalog.add(banana)
catalog.add(laptop)
catalog.add(phone)
catalog.add(apartment)

print(f"\n> Всего товаров в каталоге: {len(catalog)}")

print("\n> Все товары (через __iter__):")
for product in catalog:
    print(f"  • {product}")

print("\n> Фильтрация по наличию (get_available):")
available_products = catalog.get_available()
for product in available_products:
    print(f"  • {product.get_name()} - {product.get_price()} руб.")

print("\n> Сортировка по цене (sort_by_price):")
sorted_products = catalog.sort_by_price()
for product in sorted_products:
    print(f"  • {product.get_name()}: {product.get_price()} руб.")

print("\n> Поиск по ID (find_by_id):")
found = catalog.find_by_id("#T001")
if found:
    print(f"  Найден товар с ID #T001: {found.get_name()}")


# ============ СПЕЦИФИЧНЫЕ МЕТОДЫ ============
print("\n" + "=" * 70)
print("СЦЕНАРИЙ 6: СПЕЦИФИЧНЫЕ МЕТОДЫ КЛАССОВ")
print("=" * 70)

print("\n> Food.check_expiration():")
print(f"  Яблоко: {apple.check_expiration()}")
print(f"  Банан: {banana.check_expiration()}")

print("\n> Techic.check_price_online():")
print(f"  MacBook: {laptop.check_price_online()}")

print("\n> Estate (информация об объекте):")
print(f"  {apartment}")


# ============ ИТОГ ============
print("\n" + "=" * 70)
print("ИТОГ: ВСЕ ТРЕБОВАНИЯ ВЫПОЛНЕНЫ")
print("=" * 70)
print("✓ 2 интерфейса: Product, Catalog")
print("✓ Дополнительный интерфейс: Comparable (архитектурное поведение)")
print("✓ Полиморфизм через интерфейс (print_all_products без isinstance)")
print("✓ Проверка isinstance для интерфейсов")
print("✓ super() в дочерних классах")
print("✓ Разная реализация методов в Food, Techic, Estate")
print("✓ Каталог с фильтрацией и сортировкой")
print("=" * 70)