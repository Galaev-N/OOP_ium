from typing import List, Optional, Callable, Any, Dict
from datetime import datetime
from model_1 import Product
from new_models import Food, Technic, Estate
from container import TypedCollection
from strategies import SBP, SBN, SBI, FBQ, FBM, CS, CC
from exceptions import ItemNotFoundError, DuplicateItemError, InvalidInputError
from storage import save, load



class ShopApp:
    
    def __init__(self, storage_file: str = "data.json"):

        self.collection = TypedCollection()
        self.storage_file = storage_file
        self.model_classes = {
            'Product': Product,
            'Food': Food,
            'Technic': Technic,
            'Estate': Estate
        }
        self._load_data()
    
    def _load_data(self) -> None:
        try:
            items = load(self.storage_file, self.model_classes)
            for item in items:
                self.collection.A(item)
            print(f"Загружено {len(items)} товаров из файла")
        except StorageError as e:
            print(f"Не удалось загрузить данные: {e}")
    
    def save_data(self) -> None:
        try:
            save(self.collection.items, self.storage_file)
            print("Данные сохранены")
        except StorageError as e:
            print(f"Ошибка сохранения: {e}")
    
    def add_item(self, item: Any) -> str:
        # Проверка на дубликат
        existing = self.collection.FBI(item._id if hasattr(item, '_id') else item.id)
        if existing:
            raise DuplicateItemError(item._id)
        
        return self.collection.A(item)
    
    def remove_item(self, item_id: str) -> str:
        item = self.collection.FBI(item_id)
        if not item:
            raise ItemNotFoundError(f"Товар с ID '{item_id}' не найден")
        
        return self.collection.R(item)
    
    def remove_item_at_index(self, index: int) -> str:
        try:
            removed = self.collection.RAI(index)
            return f"Товар '{removed.name}' удален"
        except IndexError as e:
            raise ItemNotFoundError(str(e))
    
    def get_all_items(self) -> List[Any]:
        return self.collection.items
    
    def find_by_id(self, item_id: str) -> Optional[Any]:
        return self.collection.FBI(item_id)
    
    def filter_items(self, predicate: Callable[[Any], bool]) -> List[Any]:
        return self.collection.filter(predicate)
    
    def sort_items(self, key_func: Callable[[Any], Any], reverse: bool = False) -> List[Any]:
        return sorted(self.collection.items, key=key_func, reverse=reverse)
    
    def apply_transformation(self, transform: Callable[[Any], Any]) -> None:
        self.collection.apply(transform)
    
    def get_available_items(self) -> List[Any]:
        available = self.collection.GAva()
        return available.items if available else []
    
    def get_item_count(self) -> int:
        return len(self.collection)
    
    def get_sort_strategies(self) -> Dict[str, Callable]:
        return {
            "1": ("По названию", lambda x: x.name),
            "2": ("По цене", lambda x: x.price),
            "3": ("По ID", lambda x: x._id if hasattr(x, '_id') else x.id),
            "4": ("По количеству", lambda x: x.quantity if hasattr(x, 'quantity') else 0),
            "5": ("По оценке", lambda x: x.mark if hasattr(x, 'mark') else 0),
        }
    
    def get_filter_strategies(self) -> Dict[str, Callable]:
        return {
            "1": ("Только в наличии", lambda x: hasattr(x, 'quantity') and x.quantity > 0),
            "2": ("С оценкой >= 4", lambda x: hasattr(x, 'mark') and x.mark >= 4),
            "3": ("Цена <= 1000", lambda x: x.price <= 1000),
            "4": ("Цена > 5000", lambda x: x.price > 5000),
            "5": ("Только еда", lambda x: isinstance(x, Food)),
            "6": ("Только техника", lambda x: isinstance(x, Technic)),
            "7": ("Только недвижимость", lambda x: isinstance(x, Estate)),
        }