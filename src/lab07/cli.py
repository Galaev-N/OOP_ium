from model_1 import Product
from new_models import Food, Technic, Estate
from validate import *
from exceptions import *


class ConsoleUI:
    
    def __init__(self, app):
        self.app = app
    
    def show_menu(self) -> None:
        print("\n" + "=" * 60)
        print("            МАГАЗИН - КОНСОЛЬНОЕ ПРИЛОЖЕНИЕ")
        print("=" * 60)
        print("1. Добавить товар")
        print("2. Показать все товары")
        print("3. Найти товар по ID")
        print("4. Удалить товар")
        print("5. Сортировать товары")
        print("6. Фильтровать товары")
        print("7. Показать доступные товары")
        print("8. Применить трансформацию")
        print("9. Статистика")
        print("0. Выход и сохранение")
        print("-" * 60)
    
    def get_choice(self) -> str:
        while True:
            try:
                choice = input("Выберите пункт: ").strip()
                return choice
            except Exception as e:
                print(f"Ошибка: {e}")
    
    def add_item_flow(self) -> None:
        print("\n--- ДОБАВЛЕНИЕ ТОВАРА ---")
        print("Выберите тип товара:")
        print("1. Обычный товар (Product)")
        print("2. Продукт питания (Food)")
        print("3. Техника (Technic)")
        print("4. Недвижимость (Estate)")
        
        while True:
            try:
                type_choice = input("Ваш выбор (1-4): ").strip()
                
                if type_choice == "1":
                    item = self._create_product()
                elif type_choice == "2":
                    item = self._create_food()
                elif type_choice == "3":
                    item = self._create_technic()
                elif type_choice == "4":
                    item = self._create_estate()
                else:
                    print("Неверный выбор. Попробуйте снова.")
                    continue
                
                result = self.app.add_item(item)
                print(f"\n {result}")
                break
                
            except (TypeError, ValueError) as e:
                print(f"\n Ошибка валидации: {e}")
            except DuplicateItemError as e:
                print(f"\n {e}")
            except Exception as e:
                print(f"\n Неожиданная ошибка: {e}")
    
    def _create_product(self) -> Product:
        print("\n--- Введите данные товара ---")
        name = input("Название: ").strip()
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))
        producer = input("Производитель: ").strip()
        cost_price = float(input("Себестоимость: "))
        id_str = input("ID (формат #XXXXXX): ").strip()
        description = input("Описание: ").strip()
        
        return Product(
            name=name, price=price, quantity=quantity,
            producer=producer, cost_price=cost_price,
            id=id_str, description=description, comments={}
        )
    
    def _create_food(self) -> Food:
        print("\n--- Введите данные продукта питания ---")
        name = input("Название: ").strip()
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))
        producer = input("Производитель: ").strip()
        cost_price = float(input("Себестоимость: "))
        id_str = input("ID (формат #XXXXXX): ").strip()
        description = input("Описание: ").strip()
        calories = int(input("Калории: "))
        expiration_days = int(input("Срок годности (дней): "))
        
        return Food(
            name=name, price=price, quantity=quantity,
            producer=producer, cost_price=cost_price,
            id=id_str, description=description, comments={},
            calories=calories, expiration_period=expiration_days
        )
    
    def _create_technic(self) -> Technic:
        print("\n--- Введите данные техники ---")
        name = input("Название: ").strip()
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))
        producer = input("Производитель: ").strip()
        cost_price = float(input("Себестоимость: "))
        id_str = input("ID (формат #XXXXXX): ").strip()
        description = input("Описание: ").strip()
        warranty_months = int(input("Гарантия (месяцев): "))
        power = float(input("Мощность (кВт): "))
        
        return Technic(
            name=name, price=price, quantity=quantity,
            producer=producer, cost_price=cost_price,
            id=id_str, description=description, comments={},
            warranty_months=warranty_months, power=power
        )
    
    def _create_estate(self) -> Estate:
        print("\n--- Введите данные недвижимости ---")
        name = input("Название: ").strip()
        price = int(input("Цена: "))
        quantity = int(input("Количество: "))
        producer = input("Владелец: ").strip()
        cost_price = float(input("Себестоимость: "))
        id_str = input("ID (формат #XXXXXX): ").strip()
        description = input("Описание: ").strip()
        location_lat = float(input("Широта: "))
        location_lon = float(input("Долгота: "))
        area = int(input("Площадь (м²): "))
        free = input("Свободно? (1-да/0-нет): ") in ['1', 'да', 'true', 'yes']
        
        return Estate(
            name=name, price=price, quantity=quantity,
            producer=producer, cost_price=cost_price,
            id=id_str, description=description, comments={},
            location=(location_lat, location_lon), area=area, free=free
        )
    
    def show_all_items(self) -> None:
        items = self.app.get_all_items()
        
        if not items:
            print("\n Коллекция пуста!")
            return
        
        print(f"\n ВСЕ ТОВАРЫ (всего: {len(items)})")
        print("=" * 60)
        
        for i, item in enumerate(items, 1):
            print(f"\n[{i}] {item}")
            print("-" * 40)
    
    def find_item_flow(self) -> None:
        print("\n--- ПОИСК ТОВАРА ---")
        item_id = input("Введите ID товара (например #123456): ").strip()
        
        item = self.app.find_by_id(item_id)
        
        if item:
            print("\n РЕЗУЛЬТАТ ПОИСКА:")
            print("=" * 40)
            print(item)
        else:
            print(f"\n Товар с ID '{item_id}' не найден")
    
    def remove_item_flow(self) -> None:
        print("\n--- УДАЛЕНИЕ ТОВАРА ---")
        
        items = self.app.get_all_items()
        if not items:
            print("Коллекция пуста!")
            return
        
        print("Доступные товары:")
        for i, item in enumerate(items):
            print(f"  {i}. {item.name} (ID: {item._id if hasattr(item, '_id') else item.id})")
        
        try:
            choice = input("\nУдалить по (1-индекс / 2-ID): ").strip()
            
            if choice == "1":
                index = int(input("Введите индекс: "))
                print(f"\n Вы уверены?")
                confirm = input(f"Удалить товар с индексом {index}? (y/n): ").strip().lower()
                if confirm == 'y':
                    result = self.app.remove_item_at_index(index)
                    print(f"\n {result}")
                else:
                    print("Удаление отменено")
            
            elif choice == "2":
                item_id = input("Введите ID: ").strip()
                confirm = input(f"Удалить товар с ID '{item_id}'? (y/n): ").strip().lower()
                if confirm == 'y':
                    result = self.app.remove_item(item_id)
                    print(f"\n {result}")
                else:
                    print("Удаление отменено")
            
            else:
                print("Неверный выбор")
                
        except ValueError as e:
            print(f"Ошибка: {e}")
        except ItemNotFoundError as e:
            print(f"✗ {e}")
    
    def sort_items_flow(self) -> None:
        if not self.app.get_all_items():
            print("\nКоллекция пуста!")
            return
        
        print("\n--- СОРТИРОВКА ТОВАРОВ ---")
        strategies = self.app.get_sort_strategies()
        
        for key, (name, _) in strategies.items():
            print(f"{key}. {name}")
        
        try:
            choice = input("Выберите критерий сортировки: ").strip()
            reverse = input("По убыванию? (y/n): ").strip().lower() == 'y'
            
            if choice in strategies:
                _, key_func = strategies[choice]
                sorted_items = self.app.sort_items(key_func, reverse)
                
                print("\n ОТСОРТИРОВАННЫЕ ТОВАРЫ:")
                print("=" * 50)
                for i, item in enumerate(sorted_items, 1):
                    print(f"{i}. {item.name} - {item.price} руб.")
            else:
                print("Неверный выбор")
                
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def filter_items_flow(self) -> None:
        if not self.app.get_all_items():
            print("\nКоллекция пуста!")
            return
        
        print("\n--- ФИЛЬТРАЦИЯ ТОВАРОВ ---")
        strategies = self.app.get_filter_strategies()
        
        for key, (name, _) in strategies.items():
            print(f"{key}. {name}")
        
        try:
            choice = input("Выберите фильтр: ").strip()
            
            if choice in strategies:
                _, filter_func = strategies[choice]
                filtered = self.app.filter_items(filter_func)
                
                print(f"\n РЕЗУЛЬТАТЫ ФИЛЬТРАЦИИ (найдено: {len(filtered)})")
                print("=" * 50)
                for i, item in enumerate(filtered, 1):
                    print(f"{i}. {item.name} - {item.price} руб.")
                    if hasattr(item, 'quantity'):
                        print(f"   В наличии: {item.quantity}")
                    print()
            else:
                print("Неверный выбор")
                
        except Exception as e:
            print(f"Ошибка: {e}")
    
    def show_available_items(self) -> None:
        items = self.app.get_available_items()
        
        if not items:
            print("\n Нет товаров в наличии!")
            return
        
        print(f"\n ТОВАРЫ В НАЛИЧИИ (всего: {len(items)})")
        print("=" * 50)
        for i, item in enumerate(items, 1):
            print(f"{i}. {item.name} - {item.price} руб.")
            if hasattr(item, 'quantity'):
                print(f"   Осталось: {item.quantity}")
            print()
    
    def show_statistics(self) -> None:
        items = self.app.get_all_items()
        
        if not items:
            print("\nНет данных для статистики")
            return
        
        total_items = len(items)
        total_value = sum(item.price for item in items)
        avg_price = total_value / total_items if total_items > 0 else 0
        
        food_count = sum(1 for item in items if isinstance(item, Food))
        technic_count = sum(1 for item in items if isinstance(item, Technic))
        estate_count = sum(1 for item in items if isinstance(item, Estate))
        product_count = total_items - food_count - technic_count - estate_count
        
        print("\n СТАТИСТИКА МАГАЗИНА")
        print("=" * 40)
        print(f"Всего товаров: {total_items}")
        print(f"Общая стоимость: {total_value} руб.")
        print(f"Средняя цена: {avg_price:.2f} руб.")
        print(f"\nПо категориям:")
        print(f"  - Обычные товары: {product_count}")
        print(f"  - Продукты питания: {food_count}")
        print(f"  - Техника: {technic_count}")
        print(f"  - Недвижимость: {estate_count}")
    
    def run(self) -> None:
        print("\n Добро пожаловать в Магазин!")
        
        while True:
            try:
                self.show_menu()
                choice = self.get_choice()
                
                if choice == "1":
                    self.add_item_flow()
                elif choice == "2":
                    self.show_all_items()
                elif choice == "3":
                    self.find_item_flow()
                elif choice == "4":
                    self.remove_item_flow()
                elif choice == "5":
                    self.sort_items_flow()
                elif choice == "6":
                    self.filter_items_flow()
                elif choice == "7":
                    self.show_available_items()
                elif choice == "8":
                    print("\nДоступные трансформации:")
                    print("1. Инвертировать статус всех товаров")
                    print("2. Очистить комментарии")
                    trans_choice = input("Выберите: ")
                    # Здесь можно добавить трансформации
                    print("Функция в разработке")
                elif choice == "9":
                    self.show_statistics()
                elif choice == "0":
                    print("\n Сохранение данных...")
                    self.app.save_data()
                    print("До свидания!")
                    break
                else:
                    print("\n Неверный пункт меню. Попробуйте снова.")
                
                input("\nНажмите Enter для продолжения...")
                
            except KeyboardInterrupt:
                print("\n\n Принудительное завершение...")
                self.app.save_data()
                break
            except Exception as e:
                print(f"\n Непредвиденная ошибка: {e}")
                input("\nНажмите Enter для продолжения...")