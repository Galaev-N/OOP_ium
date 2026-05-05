# demo.py
from new_models import Product, Food, Technic, Estate
from new_col import ProductCatalog
from strategies import *

# ============================================================
# 1. СОЗДАНИЕ КОЛЛЕКЦИИ ОБЪЕКТОВ (минимум 5 штук)
# ============================================================

print("=" * 60)
print("1. СОЗДАНИЕ КОЛЛЕКЦИИ")
print("=" * 60)

# Создаем объекты разных типов
products = [
    Product("Ноутбук", 150000, 5, "Asus", 100000.0, "#A00001", 
            "Мощный игровой ноутбук", {"user1": "Отлично!"}, mark=4.8),
    
    Food("Яблоки", 150, 100, "Фруктовая компания", 80.0, "#F00002",
         "Свежие красные яблоки", {"user2": "Вкусно!"}, expiration_per=14, mark=4.5, calories=52),
    
    Technic("Телевизор", 50000, 3, "Samsung", 35000.0, "#T00003",
            "4K Ultra HD", {"user3": "Хороший"}, warranty_months=24, power_consumption=120.0, mark=4.2),
    
    Estate("Квартира", 5000000, "Застройщик", "#E00004",
           "Просторная квартира в центре", {}, location=(55.75, 37.62), 
           proportions=75, free=1, mark=4.9),
    
    Product("Книга", 500, 50, "Издательство", 300.0, "#A00005",
            "Интересная книга", {"user4": "Шедевр!"}, mark=4.9),
    
    Food("Молоко", 89, 200, "Молочная ферма", 50.0, "#F00006",
         "Свежее молоко", {}, expiration_per=7, mark=4.0, calories=42),
]

collection = ProductCatalog(products)
print(f"Создана коллекция из {len(collection)} объектов")
for item in collection:
    print(f"  - {item.name} ({item.__class__.__name__})")

# ============================================================
# 2. СОРТИРОВКА ТРЕМЯ РАЗНЫМИ СТРАТЕГИЯМИ
# ============================================================

print("\n" + "=" * 60)
print("2. СОРТИРОВКА КОЛЛЕКЦИИ")
print("=" * 60)

# Копируем коллекцию для демонстрации
col_for_sort = ProductCatalog(collection.items.copy())

# Стратегия 1: по цене
print("\n--- Сортировка по цене (SBP) ---")
col_for_sort.sort_by(SBP())
print([f"{item.name}: {item.price}" for item in col_for_sort])

# Стратегия 2: по имени
print("\n--- Сортировка по имени (SBN) ---")
col_for_sort = ProductCatalog(collection.items.copy())
col_for_sort.sort_by(SBN())
print([f"{item.name}" for item in col_for_sort])

# Стратегия 3: по ID
print("\n--- Сортировка по ID (SBI) ---")
col_for_sort = ProductCatalog(collection.items.copy())
col_for_sort.sort_by(SBI())
print([f"{item.name}: {item.id}" for item in col_for_sort])

# ============================================================
# 3. ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ
# ============================================================

print("\n" + "=" * 60)
print("3. ФИЛЬТРАЦИЯ КОЛЛЕКЦИИ")
print("=" * 60)

# Фильтр 1: по наличию (количество > 0)
print("\n--- Фильтр: товары в наличии (FBQ) ---")
col_for_filter = ProductCatalog(collection.items.copy())
filtered = col_for_filter.filter_by(FBQ(0))
print(f"Осталось {len(filtered)} товаров:")
for item in filtered:
    print(f"  - {item.name}: количество = {item.quantity}")

# Фильтр 2: по рейтингу >= 4.5
print("\n--- Фильтр: товары с рейтингом >= 4.5 (FBM) ---")
col_for_filter = ProductCatalog(collection.items.copy())
filtered = col_for_filter.filter_by(FBM(4.5))
print(f"Товары с высоким рейтингом:")
for item in filtered:
    print(f"  - {item.name}: рейтинг = {item.mark}")

# ============================================================
# 4. ПРИМЕНЕНИЕ MAP() — ТРАНСФОРМАЦИЯ
# ============================================================

print("\n" + "=" * 60)
print("4. ПРИМЕНЕНИЕ MAP() - ТРАНСФОРМАЦИЯ")
print("=" * 60)

print("\n--- Применение скидки 20% к ценам (через map) ---")
col_for_apply = ProductCatalog(collection.items.copy())
print("Цены до применения скидки:")
for item in col_for_apply:
    print(f"  - {item.name}: {item.price}")


# ============================================================
# 5. ИСПОЛЬЗОВАНИЕ ФАБРИКИ ФУНКЦИЙ
# ============================================================

print("\n" + "=" * 60)
print("5. ИСПОЛЬЗОВАНИЕ ФАБРИКИ ФУНКЦИЙ")
print("=" * 60)

print("\n--- Фабрика Specific_FP: фильтр по цене ---")
# Создаем фильтр для товаров дешевле 1000
cheap_filter = Specific_FP(1000)

col_for_factory = ProductCatalog(collection.items.copy())
cheap_products = col_for_factory.filter_by(cheap_filter)
print(f"Товары дешевле 1000 рублей:")
for item in cheap_products:
    print(f"  - {item.name}: {item.price}")

# ============================================================
# 6. ВЫЗОВ МЕТОДОВ sort_by() / filter_by() КОЛЛЕКЦИИ
# ============================================================

print("\n" + "=" * 60)
print("6. ВЫЗОВ МЕТОДОВ КОЛЛЕКЦИИ")
print("=" * 60)

print("\n--- Метод filter_by() ---")
col_methods = ProductCatalog(collection.items.copy())
col_methods.filter_by(lambda p: p.price < 50000)
print(f"После фильтрации (дешевле 50000): {len(col_methods)} товаров")

print("\n--- Метод sort_by() ---")
col_methods.sort_by(SBP())
print("Отсортировано по цене:")
for item in col_methods:
    print(f"  - {item.name}: {item.price}")

# ============================================================
# 7. СРАВНЕНИЕ: lambda vs ИМЕНОВАННАЯ ФУНКЦИЯ
# ============================================================

print("\n" + "=" * 60)
print("7. СРАВНЕНИЕ: lambda vs ИМЕНОВАННАЯ ФУНКЦИЯ")
print("=" * 60)

# Через lambda
print("\n--- Сортировка через lambda ---")
col_lambda = ProductCatalog(collection.items.copy())
col_lambda.sort_by(lambda p: p.price)
print([f"{item.name}: {item.price}" for item in col_lambda])

# Через именованную функцию (стратегия из файла)
print("\n--- Сортировка через именованную стратегию SBP() ---")
col_named = ProductCatalog(collection.items.copy())
col_named.sort_by(SBP())
print([f"{item.name}: {item.price}" for item in col_named])

print("\n✅ Результаты идентичны!")

# ============================================================
# 8. СЦЕНАРИЙ 1: ПОЛНАЯ ЦЕПОЧКА filter → sort → apply
# ============================================================

print("\n" + "=" * 60)
print("8. СЦЕНАРИЙ 1: ЦЕПОЧКА filter → sort → apply")
print("=" * 60)

col_chain = ProductCatalog(collection.items.copy())

print("\nШАГ 1: Исходная коллекция")
print([f"{item.name}: {item.price}" for item in col_chain])

print("\nШАГ 2: filter_by (только товары с рейтингом >= 4.0)")
col_chain.filter_by(FBM(4.0))
print([f"{item.name}: рейтинг={item.mark}" for item in col_chain])

print("\nШАГ 3: sort_by (сортировка по цене)")
col_chain.sort_by(SBP())
print([f"{item.name}: {item.price}" for item in col_chain])

# ============================================================
# 9. СЦЕНАРИЙ 2: ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА
# ============================================================

print("\n" + "=" * 60)
print("9. СЦЕНАРИЙ 2: ЗАМЕНА СТРАТЕГИИ БЕЗ ИЗМЕНЕНИЯ КОДА")
print("=" * 60)

col_replace = ProductCatalog(collection.items.copy())

print("\n--- Сортировка по цене (SBP) ---")
col_replace.sort_by(SBP())
print([f"{item.name}: {item.price}" for item in col_replace])

print("\n--- Та же коллекция, другая стратегия (SBN) ---")
col_replace.sort_by(SBN())
print([f"{item.name}" for item in col_replace])

print("\n✅ Стратегия заменена без изменения кода коллекции!")

# ============================================================
# 10. СЦЕНАРИЙ 3: callable-объект как стратегия
# ============================================================

print("\n" + "=" * 60)
print("10. СЦЕНАРИЙ 3: CALLABLE-ОБЪЕКТ КАК СТРАТЕГИЯ")
print("=" * 60)

# Создаем callable-объект стратегии
class CustomFilter:
    """Пользовательская стратегия фильтрации"""
    def __init__(self, threshold):
        self.threshold = threshold
    
    def __call__(self, product):
        return product.price > self.threshold

# Используем callable-объект
print("\n--- Фильтрация через callable-объект (цена > 5000) ---")
col_callable = ProductCatalog(collection.items.copy())
expensive_filter = CustomFilter(5000)
col_callable.filter_by(expensive_filter)
print(f"Найдено дорогих товаров: {len(col_callable)}")
for item in col_callable:
    print(f"  - {item.name}: {item.price}")

print("\n--- Трансформация через callable-объект (Change Status) ---")
col_status = ProductCatalog([collection.items[0]])  # берем один товар
print(f"Исходный статус: {col_status.items[0]._status}")
col_status.apply(CS())
print(f"Статус после CS(): {col_status.items[0]._status}")

print("\n" + "=" * 60)
print("✅ ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА УСПЕШНО!")
print("=" * 60)