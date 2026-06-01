from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Callable

try:
    from .exceptions import DuplicateItemError, ItemNotFoundError, StorageError
    from .storage import load, save
except ImportError:
    from exceptions import DuplicateItemError, ItemNotFoundError, StorageError
    from storage import load, save


def _prepare_import_paths() -> Path:
    current_file = Path(__file__).resolve()
    src_dir = current_file.parents[1]
    project_root = current_file.parents[2]
    lab05_dir = src_dir / "lab05"

    for path in (project_root, src_dir, lab05_dir):
        path_str = str(path)
        if path_str not in sys.path:
            sys.path.insert(0, path_str)

    return src_dir


def _import_project_classes() -> tuple[type[Any], type[Any], type[Any], type[Any], type[Any]]:
    src_dir = _prepare_import_paths()
    errors: list[str] = []

    collection_class: type[Any] | None = None
    for lab_name in ("lab006", "lab06"):
        try:
            module = __import__(f"src.{lab_name}.container", fromlist=["TypedCollection"])
            collection_class = module.TypedCollection
            break
        except Exception as exc:
            errors.append(f"src.{lab_name}.container: {exc}")
            try:
                lab_dir = src_dir / lab_name
                if str(lab_dir) not in sys.path:
                    sys.path.insert(0, str(lab_dir))
                module = __import__("container", fromlist=["TypedCollection"])
                collection_class = module.TypedCollection
                break
            except Exception as inner_exc:
                errors.append(f"{lab_name}/container.py: {inner_exc}")

    try:
        model_module = __import__("src.lab05.model", fromlist=["Product"])
    except Exception:
        model_module = __import__("model", fromlist=["Product"])

    try:
        models_module = __import__("src.lab05.new_models", fromlist=["Food", "Technic", "Techic", "Estate"])
    except Exception:
        models_module = __import__("new_models", fromlist=["Food", "Technic", "Techic", "Estate"])

    Product = model_module.Product
    Food = models_module.Food
    Technic = getattr(models_module, "Technic", getattr(models_module, "Techic", None))
    Estate = models_module.Estate

    if Technic is None:
        raise ImportError("В lab05.new_models не найден класс Technic/Techic")
    if collection_class is None:
        raise ImportError("Не найден TypedCollection из lab06/lab006:\n" + "\n".join(errors))

    return Product, Food, Technic, Estate, collection_class


Product, Food, Technic, Estate, TypedCollection = _import_project_classes()


class ShopApp:

    def __init__(self, storage_file: str = "shop_data.json") -> None:   
        self.storage_file: str = storage_file
        self.collection: Any = TypedCollection()
        self.model_classes: dict[str, type[Any]] = {
            "Product": Product,
            "Food": Food,
            "Technic": Technic,
            "Techic": Technic,
            "Estate": Estate,
        }
        self.load_data()

    @property
    def items(self) -> list[Any]:
        if hasattr(self.collection, "items"):
            return list(self.collection.items)
        return list(self.collection)

    def load_data(self) -> None:
        try:
            loaded_items = load(self.storage_file, self.model_classes)
            for item in loaded_items:
                self._add_raw(item)
            print(f"Автозагрузка: {len(loaded_items)} объектов")
        except StorageError as exc:
            print(f"Ошибка загрузки: {exc}")

    def save_data(self) -> None:
        save(self.items, self.storage_file)

    def _add_raw(self, item: Any) -> None:
        if hasattr(self.collection, "add"):
            self.collection.add(item)
        elif hasattr(self.collection, "A"):
            self.collection.A(item)
        else:
            self.collection.items.append(item)

    def get_item_id(self, item: Any) -> str:
        return str(getattr(item, "_id", getattr(item, "id", "")))

    def get_item_name(self, item: Any) -> str:
        return str(getattr(item, "name", getattr(item, "_name", "Без названия")))

    def get_item_price(self, item: Any) -> int:
        return int(getattr(item, "price", getattr(item, "_price", 0)))

    def get_item_quantity(self, item: Any) -> int:
        return int(getattr(item, "quantity", getattr(item, "_quantity", 0)))

    def get_item_mark(self, item: Any) -> float:
        return float(getattr(item, "mark", getattr(item, "_mark", 0.0)))

    def add_item(self, item: Any) -> str:
        item_id = self.get_item_id(item)
        if self.find_by_id(item_id) is not None:
            raise DuplicateItemError(item_id)
        self._add_raw(item)
        return f"Товар '{self.get_item_name(item)}' добавлен"

    def remove_item(self, item_id: str) -> str:
        item = self.find_by_id(item_id)
        if item is None:
            raise ItemNotFoundError(f"Товар с ID '{item_id}' не найден")
        if hasattr(self.collection, "remove"):
            self.collection.remove(item)
        elif hasattr(self.collection, "R"):
            self.collection.R(item)
        else:
            self.collection.items.remove(item)
        return f"Товар '{self.get_item_name(item)}' удален"

    def remove_item_at_index(self, index: int) -> str:
        """Удаляет объект по индексу, где index начинается с 0."""
        try:
            if hasattr(self.collection, "remove_at_index"):
                item = self.collection.remove_at_index(index)
            elif hasattr(self.collection, "RAI"):
                item = self.collection.RAI(index)
            else:
                item = self.collection.items.pop(index)
            return f"Товар '{self.get_item_name(item)}' удален"
        except IndexError as exc:
            raise ItemNotFoundError("Индекс вне диапазона") from exc

    def get_all_items(self) -> list[Any]:
        """Возвращает все товары."""
        return self.items

    def find_by_id(self, item_id: str) -> Any | None:
        """Ищет товар по ID."""
        for item in self.items:
            if self.get_item_id(item) == item_id:
                return item
        return None

    def sort_items(self, key_func: Callable[[Any], Any], reverse: bool = False) -> list[Any]:
        """Возвращает отсортированный список товаров."""
        return sorted(self.items, key=key_func, reverse=reverse)

    def filter_items(self, predicate: Callable[[Any], bool]) -> list[Any]:
        """Возвращает список товаров, подходящих под условие."""
        return [item for item in self.items if predicate(item)]

    def get_available_items(self) -> list[Any]:
        """Возвращает доступные товары."""
        def is_available(item: Any) -> bool:
            if hasattr(item, "free"):
                return bool(getattr(item, "free"))
            return self.get_item_quantity(item) > 0

        return self.filter_items(is_available)

    def invert_status(self) -> None:
        """Инвертирует статус всех объектов."""
        for item in self.items:
            current = bool(getattr(item, "_status", 0))
            setattr(item, "_status", int(not current))

    def clear_comments(self) -> None:
        """Очищает комментарии у всех объектов."""
        for item in self.items:
            if hasattr(item, "comments"):
                item.comments = {}

    def get_sort_strategies(self) -> dict[str, tuple[str, Callable[[Any], Any]]]:
        """Возвращает стратегии сортировки для меню."""
        return {
            "1": ("По названию", self.get_item_name),
            "2": ("По цене", self.get_item_price),
            "3": ("По ID", self.get_item_id),
            "4": ("По количеству", self.get_item_quantity),
            "5": ("По оценке", self.get_item_mark),
        }

    def get_filter_strategies(self) -> dict[str, tuple[str, Callable[[Any], bool]]]:
        """Возвращает стратегии фильтрации для меню."""
        return {
            "1": ("Только в наличии", lambda item: item in self.get_available_items()),
            "2": ("Оценка >= 4", lambda item: self.get_item_mark(item) >= 4),
            "3": ("Цена <= 1000", lambda item: self.get_item_price(item) <= 1000),
            "4": ("Цена > 5000", lambda item: self.get_item_price(item) > 5000),
            "5": ("Только продукты питания", lambda item: isinstance(item, Food)),
            "6": ("Только техника", lambda item: isinstance(item, Technic)),
            "7": ("Только недвижимость", lambda item: isinstance(item, Estate)),
        }

    def get_statistics(self) -> dict[str, Any]:
        """Возвращает статистику по коллекции."""
        items = self.items
        total_price = sum(self.get_item_price(item) for item in items)
        return {
            "total": len(items),
            "total_price": total_price,
            "average_price": total_price / len(items) if items else 0,
            "product": sum(type(item).__name__ == "Product" for item in items),
            "food": sum(isinstance(item, Food) for item in items),
            "technic": sum(isinstance(item, Technic) for item in items),
            "estate": sum(isinstance(item, Estate) for item in items),
        }
