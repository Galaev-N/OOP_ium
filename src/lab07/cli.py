"""Консольный интерфейс для ЛР-7."""

from __future__ import annotations

from typing import Any

try:
    from .app import Estate, Food, Product, ShopApp, Technic
    from .exceptions import DuplicateItemError, InvalidInputError, ItemNotFoundError, StorageError
except ImportError:
    from app import Estate, Food, Product, ShopApp, Technic
    from exceptions import DuplicateItemError, InvalidInputError, ItemNotFoundError, StorageError


class ConsoleUI:
    """CLI-оболочка: отвечает только за ввод и вывод."""

    def __init__(self, app: ShopApp) -> None:
        """Создает интерфейс для объекта приложения."""
        self.app: ShopApp = app

    def show_menu(self) -> None:
        """Показывает главное меню."""
        print("\n" + "=" * 62)
        print("              МАГАЗИН: ЛАБОРАТОРНАЯ 7")
        print("=" * 62)
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
        print("-" * 62)

    def read_str(self, prompt: str) -> str:
        """Считывает непустую строку."""
        value = input(prompt).strip()
        if not value:
            raise InvalidInputError("Поле не может быть пустым")
        return value

    def read_int(self, prompt: str) -> int:
        """Считывает целое число."""
        try:
            return int(input(prompt).strip())
        except ValueError as exc:
            raise InvalidInputError("Нужно ввести целое число") from exc

    def read_float(self, prompt: str) -> float:
        """Считывает число с плавающей точкой."""
        try:
            return float(input(prompt).strip())
        except ValueError as exc:
            raise InvalidInputError("Нужно ввести число") from exc

    def read_yes_no(self, prompt: str) -> bool:
        """Считывает подтверждение действия."""
        return input(prompt).strip().lower() in {"y", "yes", "д", "да", "1"}

    def add_item_flow(self) -> None:
        """Добавляет товар выбранного типа."""
        print("\n--- ДОБАВЛЕНИЕ ТОВАРА ---")
        print("1. Обычный товар")
        print("2. Продукт питания")
        print("3. Техника")
        print("4. Недвижимость")
        print("0. Назад")

        try:
            choice = input("Выберите тип: ").strip()
            if choice == "0":
                return
            if choice == "1":
                item = self._create_product()
            elif choice == "2":
                item = self._create_food()
            elif choice == "3":
                item = self._create_technic()
            elif choice == "4":
                item = self._create_estate()
            else:
                raise InvalidInputError("Неверный тип товара")
            print(self.app.add_item(item))
        except (InvalidInputError, ValueError, TypeError, DuplicateItemError) as exc:
            print(f"Ошибка: {exc}")

    def _read_common_fields(self) -> dict[str, Any]:
        """Считывает общие поля для Product, Food и Technic."""
        return {
            "name": self.read_str("Название: "),
            "price": self.read_int("Цена: "),
            "quantity": self.read_int("Количество: "),
            "producer": self.read_str("Производитель: "),
            "cost_price": self.read_float("Себестоимость: "),
            "id": self.read_str("ID (формат #XXXXXX): "),
            "description": self.read_str("Описание: "),
            "comments": {},
            "mark": self.read_float("Оценка (0-5): "),
        }

    def _create_product(self) -> Product:
        """Создает обычный товар."""
        print("\n--- Данные обычного товара ---")
        return Product(**self._read_common_fields())

    def _create_food(self) -> Food:
        """Создает продукт питания. Исправлено: используется expiration_per."""
        print("\n--- Данные продукта питания ---")
        data = self._read_common_fields()
        calories = self.read_int("Калории: ")
        expiration_days = self.read_int("Срок годности (дней): ")
        return Food(**data, expiration_per=expiration_days, calories=calories)

    def _create_technic(self) -> Technic:
        """Создает объект техники."""
        print("\n--- Данные техники ---")
        data = self._read_common_fields()
        warranty_months = self.read_int("Гарантия (месяцев): ")
        power_consumption = self.read_float("Потребление энергии: ")
        return Technic(**data, warranty_months=warranty_months, power_consumption=power_consumption)

    def _create_estate(self) -> Estate:
        """Создает объект недвижимости."""
        print("\n--- Данные недвижимости ---")
        return Estate(
            name=self.read_str("Название: "),
            price=self.read_int("Цена: "),
            producer=self.read_str("Владелец/застройщик: "),
            id=self.read_str("ID (формат #XXXXXX): "),
            description=self.read_str("Описание: "),
            comments={},
            location=(self.read_float("Широта: "), self.read_float("Долгота: ")),
            proportions=self.read_int("Площадь: "),
            free=1 if self.read_yes_no("Свободно? (y/n): ") else 0,
            mark=self.read_float("Оценка (0-5): "),
        )

    def show_all_items(self) -> None:
        """Показывает все товары."""
        self._print_items(self.app.get_all_items(), "ВСЕ ТОВАРЫ")

    def find_item_flow(self) -> None:
        """Ищет товар по ID."""
        try:
            item_id = self.read_str("\nВведите ID: ")
            item = self.app.find_by_id(item_id)
            if item is None:
                print(f"Товар с ID '{item_id}' не найден")
                return
            self._print_items([item], "РЕЗУЛЬТАТ ПОИСКА")
        except InvalidInputError as exc:
            print(f"Ошибка: {exc}")

    def remove_item_flow(self) -> None:
        """Удаляет товар с подтверждением."""
        items = self.app.get_all_items()
        if not items:
            print("Коллекция пуста")
            return

        self._print_items(items, "ДОСТУПНЫЕ ТОВАРЫ")
        print("1. Удалить по индексу")
        print("2. Удалить по ID")
        print("0. Назад")

        try:
            choice = input("Выберите способ: ").strip()
            if choice == "0":
                return
            if choice == "1":
                index = self.read_int("Номер в таблице: ") - 1
                item = items[index]
                if self.read_yes_no(f"Удалить '{self.app.get_item_name(item)}'? (y/n): "):
                    print(self.app.remove_item_at_index(index))
                else:
                    print("Удаление отменено")
            elif choice == "2":
                item_id = self.read_str("ID: ")
                item = self.app.find_by_id(item_id)
                if item is None:
                    raise ItemNotFoundError(f"Товар с ID '{item_id}' не найден")
                if self.read_yes_no(f"Удалить '{self.app.get_item_name(item)}'? (y/n): "):
                    print(self.app.remove_item(item_id))
                else:
                    print("Удаление отменено")
            else:
                raise InvalidInputError("Неверный пункт")
        except (IndexError, InvalidInputError, ItemNotFoundError) as exc:
            print(f"Ошибка: {exc}")

    def sort_items_flow(self) -> None:
        """Сортирует товары по выбранной стратегии."""
        strategies = self.app.get_sort_strategies()
        print("\n--- СОРТИРОВКА ---")
        for key, (name, _) in strategies.items():
            print(f"{key}. {name}")
        print("0. Назад")

        choice = input("Выберите стратегию: ").strip()
        if choice == "0":
            return
        if choice not in strategies:
            print("Неверный пункт")
            return
        reverse = self.read_yes_no("По убыванию? (y/n): ")
        _, key_func = strategies[choice]
        self._print_items(self.app.sort_items(key_func, reverse), "РЕЗУЛЬТАТ СОРТИРОВКИ")

    def filter_items_flow(self) -> None:
        """Фильтрует товары по выбранной стратегии."""
        strategies = self.app.get_filter_strategies()
        print("\n--- ФИЛЬТРАЦИЯ ---")
        for key, (name, _) in strategies.items():
            print(f"{key}. {name}")
        print("0. Назад")

        choice = input("Выберите фильтр: ").strip()
        if choice == "0":
            return
        if choice not in strategies:
            print("Неверный пункт")
            return
        _, predicate = strategies[choice]
        self._print_items(self.app.filter_items(predicate), "РЕЗУЛЬТАТ ФИЛЬТРАЦИИ")

    def show_available_items(self) -> None:
        """Показывает доступные товары."""
        self._print_items(self.app.get_available_items(), "ДОСТУПНЫЕ ТОВАРЫ")

    def transform_flow(self) -> None:
        """Применяет трансформацию к коллекции."""
        print("\n--- ТРАНСФОРМАЦИИ ---")
        print("1. Инвертировать статус всех товаров")
        print("2. Очистить комментарии")
        print("0. Назад")
        choice = input("Выберите: ").strip()
        if choice == "1":
            self.app.invert_status()
            print("Статусы изменены")
        elif choice == "2":
            if self.read_yes_no("Очистить комментарии у всех товаров? (y/n): "):
                self.app.clear_comments()
                print("Комментарии очищены")
            else:
                print("Операция отменена")
        elif choice == "0":
            return
        else:
            print("Неверный пункт")

    def show_statistics(self) -> None:
        """Показывает статистику магазина."""
        stats = self.app.get_statistics()
        print("\n--- СТАТИСТИКА ---")
        print(f"Всего товаров: {stats['total']}")
        print(f"Общая стоимость: {stats['total_price']} руб.")
        print(f"Средняя цена: {stats['average_price']:.2f} руб.")
        print(f"Обычные товары: {stats['product']}")
        print(f"Продукты питания: {stats['food']}")
        print(f"Техника: {stats['technic']}")
        print(f"Недвижимость: {stats['estate']}")

    def _print_items(self, items: list[Any], title: str) -> None:
        """Печатает товары в виде простой таблицы."""
        print(f"\n{title}")
        print("-" * 96)
        print(f"{'№':<4}{'Тип':<14}{'ID':<10}{'Название':<28}{'Цена':<12}{'Кол-во/статус':<16}{'Оценка':<8}")
        print("-" * 96)
        if not items:
            print("Нет данных")
        for number, item in enumerate(items, 1):
            item_type = type(item).__name__
            item_id = self.app.get_item_id(item)
            name = self.app.get_item_name(item)[:27]
            price = self.app.get_item_price(item)
            if hasattr(item, "free"):
                amount = "свободно" if getattr(item, "free") else "занято"
            else:
                amount = str(self.app.get_item_quantity(item))
            mark = self.app.get_item_mark(item)
            print(f"{number:<4}{item_type:<14}{item_id:<10}{name:<28}{price:<12}{amount:<16}{mark:<8.1f}")
        print("-" * 96)

    def run(self) -> None:
        """Запускает основной цикл приложения."""
        print("\nЗапуск консольного приложения магазина")
        while True:
            try:
                self.show_menu()
                choice = input("Выберите пункт: ").strip()

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
                    self.transform_flow()
                elif choice == "9":
                    self.show_statistics()
                elif choice == "0":
                    self.app.save_data()
                    print("Данные сохранены. Выход.")
                    break
                else:
                    print("Неверный пункт меню")

                input("\nНажмите Enter для продолжения...")
            except KeyboardInterrupt:
                print("\nПринудительное завершение. Сохраняю данные...")
                self.app.save_data()
                break
            except StorageError as exc:
                print(f"Ошибка файла: {exc}")
            except Exception as exc:
                print(f"Непредвиденная ошибка: {exc}")
