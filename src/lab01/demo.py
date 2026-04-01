from model import Product

#============= ТЕСТ 1: КОРРЕКТНОЕ СОЗДАНИЕ ОБЪЕКТОВ =============#

try:
    # Создаем первый продукт со всеми параметрами
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
    
    # Создаем второй продукт с оценкой по умолчанию
    mouse = Product(
        name="Мышь Logitech",
        price=2500,
        quantity=20,
        producer="Logitech",
        cost_price=1800.0,
        id="#M67890",
        description="Беспроводная мышь",
        comments={},
        # mark не указан - будет 3.0 по умолчанию
    )
    
    # Создаем третий продукт с пустыми комментариями
    keyboard = Product(
        name="Клавиатура Mechanical",
        price=5000,
        quantity=0,  # Нет в наличии
        producer="HyperX",
        cost_price=3500.0,
        id="#K34567",
        description="Механическая клавиатура с RGB подсветкой",
        comments={},
        mark=4.8
    )
    product_created = True
    
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка при создании продуктов: {e}")
    product_created = False
    laptop = mouse = keyboard = None

# ============= ТЕСТ 2: МЕТОД __str__ =============
if product_created:
    print("\nМЕТОД __str__")
    print("laptop:", laptop)
    print("mouse:", mouse)
    print("keyboard:", keyboard)

# ============= ТЕСТ 3: МЕТОД __repr__ =============
if product_created:
    print("\nМЕТОД __repr__")
    print("laptop:", repr(laptop))
    print("mouse:", repr(mouse))
    print("keyboard:", repr(keyboard))

# ============= ТЕСТ 4: МЕТОД __eq__ (СРАВНЕНИЕ) =============
if product_created:
    print("\nМЕТОД __eq__ (СРАВНЕНИЕ)")
    
    # Создаем продукт с таким же именем как у laptop
    try:
        laptop2 = Product(
            name="Ноутбук ASUS",  # То же имя
            price=80000,
            quantity=3,
            producer="ASUS",
            cost_price=65000.0,
            id="#B54321",
            description="Другая модель",
            comments={},
            mark=4.2
        )
        
        print(f"laptop == laptop2 (одинаковые имена): {laptop == laptop2}")  # True
        print(f"laptop == mouse (разные имена): {laptop == mouse}")  # False
        print(f"laptop == keyboard (разные имена): {laptop == keyboard}")  # False
        
        # Сравнение с объектом другого типа
        print(f"laptop == 'Ноутбук ASUS': {laptop == 'Ноутбук ASUS'}")  # False
        
    except (TypeError, ValueError) as e:
        print(f"Ошибка при создании laptop2: {e}")

# ============= ТЕСТ 5: PROPERTY INFO =============
if product_created:
    print("\nPROPERTY INFO")
    
    print("laptop.info:")
    print(laptop.info)
    print("\nmouse.info:")
    print(mouse.info)
    print("\nkeyboard.info:")
    print(keyboard.info)

# ============= ТЕСТ 6: PROPERTY MARK (ГЕТТЕР И СЕТТЕР) =============
if product_created:
    print("\nPROPERTY SETTER/GETTER")
    
    print(f"Начальная оценка laptop: {laptop.mark}")
    print(f"Начальная оценка mouse: {mouse.mark}")
    print(f"Начальная оценка keyboard: {keyboard.mark}")
    
    # Изменяем оценки через сеттер
    print("\nИзменяем оценки:")
    laptop.mark = 5.0
    mouse.mark = 4.2
    keyboard.mark = 4.9
    
    print(f"Новая оценка laptop: {laptop.mark}")
    print(f"Новая оценка mouse: {mouse.mark}")
    print(f"Новая оценка keyboard: {keyboard.mark}")

# ============= ТЕСТ 7: МЕТОД FEEDBACK (ДОБАВЛЕНИЕ КОММЕНТАРИЕВ) =============
if product_created:
    print("\nМЕТОД FEEDBACK")
    
    print("Добавляем комментарии к laptop:")
    print(laptop.feadback("Отличный ноутбук, работает быстро!"))
    print(laptop.feadback("Батарея держит 5 часов"))
    print(laptop.feadback("Еще один комментарий"))
    
    print(f"\nТеперь у laptop {len(laptop.comments)} комментариев:")
    for user, comment in laptop.comments.items():
        print(f"  {user}: {comment}")
    
    print("\nДобавляем комментарии к mouse (начально пусто):")
    print(mouse.feadback("Удобная мышь"))
    print(mouse.feadback("Работает отлично"))
    print(mouse.feadback("Кнопки мягкие"))
    
    print(f"\nТеперь у mouse {len(mouse.comments)} комментариев:")
    for user, comment in mouse.comments.items():
        print(f"  {user}: {comment}")



# ============= ТЕСТ 8: ДОСТУП К РАЗНЫМ ТИПАМ АТРИБУТОВ =============
if product_created:
    print("\nДОСТУП К АТРИБУТАМ")
    
    print("Публичные атрибуты (доступны всегда):")
    print(f"  laptop.name = {laptop.name}")
    print(f"  laptop.price = {laptop.price}")
    print(f"  laptop.quantity = {laptop.quantity}")
    print(f"  laptop.producer = {laptop.producer}")
    print(f"  laptop.description = {laptop.description}")
    
    print("\nЗащищенный атрибут (по соглашению - внутренний):")
    print(f"  laptop._id = {laptop._id}")
    
    print("\nПриватный атрибут (доступ через name mangling):")
    print(f"  laptop._Product__cost_price__ = {laptop.__cost_price__}")

# ============= ТЕСТ 9: НЕКОРРЕКТНОЕ СОЗДАНИЕ ОБЪЕКТОВ =============
print("\nНЕКОРРЕКТНОЕ СОЗДАНИЕ ОБЪЕКТОВ (ОШИБКИ)")

# Тест 9.1: Пустое имя
print("\n10.1 Попытка создать продукт с пустым именем:")
try:
    bad_product = Product(
        name="",  # Пустое имя
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.2: Имя не строка
print("\n10.2 Попытка создать продукт с именем-числом:")
try:
    bad_product = Product(
        name=12345,  # Число вместо строки
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.3: Отрицательная цена
print("\n10.3 Попытка создать продукт с отрицательной ценой:")
try:
    bad_product = Product(
        name="Тест",
        price=-1000,  # Отрицательная цена
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.4: Цена не целое число
print("\n10.4 Попытка создать продукт с ценой-строкой:")
try:
    bad_product = Product(
        name="Тест",
        price="1000",  # Строка вместо числа
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.5: Отрицательное количество
print("\n10.5 Попытка создать продукт с отрицательным количеством:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=-5,  # Отрицательное количество
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.6: Неверный формат ID
print("\n10.6 Попытка создать продукт с неверным ID:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="12345",  # Не начинается с # и не 7 символов
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.7: Пустой производитель
print("\n10.7 Попытка создать продукт с пустым производителем:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="",  # Пустой производитель
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.8: Себестоимость не float
print("\n10.8 Попытка создать продукт с себестоимостью-строкой:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="Test",
        cost_price="500",  # Строка вместо float
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.9: Отрицательная себестоимость
print("\n10.9 Попытка создать продукт с отрицательной себестоимостью:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=-500.0,  # Отрицательная себестоимость
        id="#T00001",
        description="Тестовый продукт",
        comments={}
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# Тест 9.10: Оценка вне диапазона
print("\n10.10 Попытка создать продукт с оценкой >5:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={},
        mark=6.0  # Оценка больше 5
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

print("\n10.11 Попытка создать продукт с оценкой <0:")
try:
    bad_product = Product(
        name="Тест",
        price=1000,
        quantity=10,
        producer="Test",
        cost_price=500.0,
        id="#T00001",
        description="Тестовый продукт",
        comments={},
        mark=-1.0  # Оценка меньше 0
    )
    print("✓ Странно, продукт создался")
except (TypeError, ValueError) as e:
    print(f"✗ Ошибка поймана: {e}")

# ============= ТЕСТ 10: НЕКОРРЕКТНОЕ ИЗМЕНЕНИЕ АТРИБУТОВ =============
if product_created:
    print("\nНЕКОРРЕКТНОЕ ИЗМЕНЕНИЕ АТРИБУТОВ")
    
    # 10.1 Попытка установить некорректную оценку
    print("\n11.1 Попытка установить оценку >5 через сеттер:")
    try:
        laptop.mark = 6.0
        print("✓ Странно, оценка изменилась")
    except (TypeError, ValueError) as e:
        print(f"✗ Ошибка поймана: {e}")
    
    print("\n11.2 Попытка установить оценку <0 через сеттер:")
    try:
        laptop.mark = -1.0
        print("✓ Странно, оценка изменилась")
    except (TypeError, ValueError) as e:
        print(f"✗ Ошибка поймана: {e}")
    
    print("\n11.3 Попытка установить оценку-строку:")
    try:
        laptop.mark = "пять"
        print("✓ Странно, оценка изменилась")
    except (TypeError, ValueError) as e:
        print(f"✗ Ошибка поймана: {e}")
    
    # 10.4 Попытка вызвать mark как функцию
    print("\n11.4 Попытка вызвать mark как функцию (частая ошибка):")
    try:
        # Это вызовет ошибку, если попытаться
        print("Пытаемся: laptop.mark(5)")
        print("Результат:", laptop.mark(5))
    except TypeError as e:
        print(f"✗ Ошибка поймана: {e} - mark это число, а не метод!")

# ============= ТЕСТ 11: ФИНАЛЬНОЕ СОСТОЯНИЕ =============
if product_created:
    print("\nФИНАЛЬНОЕ СОСТОЯНИЕ ПРОДУКТОВ")
    
    print("LAPTOP:")
    print(laptop.info)
    print("\nMOUSE:")
    print(mouse.info)
    print("\nKEYBOARD:")
    print(keyboard.info)
