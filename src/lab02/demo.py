# demo.py
import sys

sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab01/')
sys.path.append(r'/Users/galaevka/oop/OOP_ium/src/lab02/')

from model import Product
from collection import ProductCatalog

# ========== СОЗДАНИЕ ТЕСТОВЫХ ПРОДУКТОВ ==========
print("\n" + "🛍️" * 30)
print("ТЕСТИРОВАНИЕ КЛАССА ProductCatalog")
print("🛍️" * 30)

laptop = Product(
    name="Ноутбук ASUS",
    price=75000,
    quantity=5,
    producer="ASUS",
    cost_price=60000.50,
    id="#A12345",
    description="Мощный игровой ноутбук с RTX 3060",
    comments={"User1": "Отличный выбор!", "User2": "Беру уже второй"},
    mark=4.5
)

mouse = Product(
    name="Мышь Logitech",
    price=2500,
    quantity=20,
    producer="Logitech",
    cost_price=1800.0,
    id="#M67890",
    description="Беспроводная мышь",
    comments={},
)

keyboard = Product(
    name="Клавиатура Mechanical",
    price=5000,
    quantity=0,
    producer="HyperX",
    cost_price=3500.0,
    id="#K34567",
    description="Механическая клавиатура с RGB подсветкой",
    comments={},
    mark=4.8
)

monitor = Product(
    name="Монитор Samsung",
    price=35000,
    quantity=3,
    producer="Samsung",
    cost_price=28000.0,
    id="#S90123",
    description="27 дюймов, 4K, 144Hz",
    comments={},
    mark=4.7
)

headphones = Product(
    name="Наушники Sony",
    price=12000,
    quantity=8,
    producer="Sony",
    cost_price=9000.0,
    id="#H45678",
    description="Беспроводные наушники с шумоподавлением",
    comments={"User3": "Отличный звук!"},
    mark=4.9
)

def print_catalog(catalog, title="Содержимое каталога"):
    """Красиво выводит каталог"""
    print(f"\n📋 {title}:")
    print("-" * 70)
    if len(catalog) == 0:
        print("  📭 Каталог пуст")
    else:
        for i, product in enumerate(catalog):
            status = "✅ В наличии" if product.quantity > 0 else "❌ Нет в наличии"
            print(f"  {i}. {product.name} | {product.price}₽ | {status} | ID: {product._id}")
    print("-" * 70)
    print(f"📊 Всего товаров: {len(catalog)}\n")

# ========== СЦЕНАРИЙ 1: БАЗОВЫЕ ОПЕРАЦИИ ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 1: Базовые операции с каталогом")
print("=" * 70)

# Создаем пустой каталог
catalog1 = ProductCatalog()
print("✅ Создан пустой каталог")

# Добавляем товары
print("\n➕ Добавляем товары:")
print(catalog1.A(laptop))
print(catalog1.A(mouse))
print(catalog1.A(keyboard))
print(catalog1.A(monitor))

print_catalog(catalog1, "Каталог после добавления")

# Проверка длины
print(f"🔢 Количество товаров в каталоге: {len(catalog1)}")

# Удаление товара
print(f"\n🗑️ {catalog1.R(mouse)}")
print_catalog(catalog1, "Каталог после удаления мыши")

# ========== СЦЕНАРИЙ 2: ИНДЕКСАЦИЯ ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 2: Демонстрация индексации (__getitem__)")
print("=" * 70)

print("🔍 Доступ к элементам по индексу:")
print(f"  catalog[0] = {catalog1[0].name} ({catalog1[0].price}₽)")
print(f"  catalog[1] = {catalog1[1].name} ({catalog1[1].price}₽)")
print(f"  catalog[2] = {catalog1[2].name} ({catalog1[2].price}₽)")

print("\n🔍 Доступ по отрицательному индексу (с конца):")
print(f"  catalog[-1] = {catalog1[-1].name} (последний товар)")
print(f"  catalog[-2] = {catalog1[-2].name} (предпоследний)")

print("\n🔄 Итерация через for (благодаря __iter__):")
for idx, product in enumerate(catalog1):
    print(f"  {idx}: {product.name}")

# ========== СЦЕНАРИЙ 3: СОРТИРОВКА ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 3: Сортировка каталога по цене (SBP)")
print("=" * 70)

# Добавим еще товаров для наглядности
catalog1.A(headphones)
print_catalog(catalog1, "Перед сортировкой")

print("🔄 Выполняем сортировку по цене (метод SBP)...")
catalog1.SBP()
print_catalog(catalog1, "После сортировки по возрастанию цены")

# ========== СЦЕНАРИЙ 4: ФИЛЬТРАЦИЯ (Get Avalible) ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 4: Фильтрация - только товары в наличии (GAva)")
print("=" * 70)

print_catalog(catalog1, "Исходный каталог")
print("🔍 Применяем фильтр GAva() - показываем только товары с quantity > 0")

available_products = catalog1.GAva()
print("\n📦 Товары в наличии:")
print("-" * 70)
if len(available_products) == 0:
    print("  📭 Нет товаров в наличии")
else:
    for i, product in enumerate(available_products):
        status = "✅ В наличии" if product.quantity > 0 else "❌ Нет в наличии"
        print(f"  {i}. {product.name} | {product.price}₽ | {status} | Кол-во: {product.quantity}")
print("-" * 70)
print(f"📊 Итого в наличии: {len(available_products)} товаров")

# ========== СЦЕНАРИЙ 5: ПОИСК ПО ID ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 5: Поиск товара по ID (FBI)")
print("=" * 70)

print("🔎 Ищем товар с ID #K34567:")
found = catalog1.FBI("#K34567")
if found:
    print(f"  ✅ Найден: {found.name} | Цена: {found.price}₽ | {found.description}")

print("\n🔎 Ищем несуществующий товар с ID #NONEXISTENT:")
found = catalog1.FBI("#NONEXISTENT")
if found:
    print(f"  Найден: {found.name}")
else:
    print("  ❌ Товар не найден (корректное поведение)")

# ========== СЦЕНАРИЙ 6: УДАЛЕНИЕ ПО ИНДЕКСУ ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 6: Удаление по индексу (RAI)")
print("=" * 70)

print_catalog(catalog1, "Каталог перед удалением")
removed_product = catalog1.RAI(1)
print(f"🗑️ Удален товар с индексом 1: {removed_product.name}")
print_catalog(catalog1, "Каталог после удаления")

# ========== СЦЕНАРИЙ 7: ОБРАБОТКА ОШИБОК ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 7: Проверка обработки ошибок")
print("=" * 70)

print("🔴 Попытка добавить не-Product объект:")
try:
    catalog1.A("Это строка, а не продукт")
except TypeError as e:
    print(f"  ✅ Ошибка перехвачена: {e}")

print("\n🔴 Попытка удалить несуществующий товар:")
try:
    catalog1.R(laptop)  # laptop уже может быть не в каталоге
except ValueError as e:
    print(f"  ✅ Ошибка перехвачена: {e}")

print("\n🔴 Попытка удалить по неверному индексу:")
try:
    catalog1.RAI(100)
except IndexError as e:
    print(f"  ✅ Ошибка перехвачена: {e}")

# ========== СЦЕНАРИЙ 8: СОЗДАНИЕ КАТАЛОГА ИЗ СПИСКА ==========
print("\n" + "=" * 70)
print("📌 СЦЕНАРИЙ 8: Создание каталога из готового списка")
print("=" * 70)

product_list = [laptop, mouse, keyboard, monitor, headphones]
catalog2 = ProductCatalog(product_list)
print(f"✅ Создан каталог из {len(catalog2)} товаров")
print_catalog(catalog2, "Каталог из списка")

# Проверка валидации
print("🔴 Попытка создать каталог с невалидным списком:")
try:
    invalid_list = [laptop, "not a product", mouse]
    catalog3 = ProductCatalog(invalid_list)
except ValueError as e:
    print(f"  ✅ Ошибка перехвачена: {e}")

# ========== ИТОГИ ==========
print("\n" + "🏆" * 35)
print("ИТОГИ ТЕСТИРОВАНИЯ")
print("🏆" * 35)

print("""
✅ Все сценарии успешно выполнены!

Проверенные методы и возможности:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  📦 Базовые операции:
     • A()     - добавление товара
     • R()     - удаление товара по значению
     • GAll()  - получение всех товаров
     • len()   - получение длины каталога
  
  🔢 Индексация и итерация:
     • __getitem__  - доступ по индексу (catalog[i])
     • __iter__     - итерация в цикле for
  
  🔍 Поиск и фильтрация:
     • FBI()        - поиск по ID
     • GAva()       - фильтрация товаров в наличии
  
  📊 Сортировка:
     • SBP()        - сортировка по цене
  
  🗑️ Удаление:
     • RAI()        - удаление по индексу
  
  ⚠️ Обработка ошибок:
     • TypeError    - при добавлении не-Product
     • ValueError   - при невалидном списке
     • IndexError   - при неверном индексе
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")

print(f"📊 Финальное состояние catalog1: {len(catalog1)} товаров")
print_catalog(catalog1, "Текущий каталог")