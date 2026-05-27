import json
import os
from typing import List, Dict, Any
from exceptions import StorageError


def save(collection: List[Any], filepath: str) -> None:
    try:
        data = []
        for item in collection:
            if hasattr(item, '__dict__'):
                # Преобразуем объект в словарь
                item_dict = {}
                for key, value in item.__dict__.items():
                    if key.startswith(f'_{item.__class__.__name__}__'):
                        # Обработка приватных атрибутов
                        actual_key = key.split('__')[-1]
                        item_dict[actual_key] = value
                    elif key.startswith('_'):
                        # Защищенные атрибуты
                        item_dict[key[1:]] = value
                    else:
                        item_dict[key] = value
                item_dict['__class__'] = item.__class__.__name__
                data.append(item_dict)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        raise StorageError(f"Ошибка сохранения: {str(e)}")


def load(filepath: str, model_classes: Dict[str, Any]) -> List[Any]:
    if not os.path.exists(filepath):
        return []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        items = []
        for item_dict in data:
            class_name = item_dict.pop('__class__', 'Product')
            
            # Определяем класс
            if class_name in model_classes:
                cls = model_classes[class_name]
                # Создаем объект с параметрами
                try:
                    obj = cls(**item_dict)
                    items.append(obj)
                except Exception as e:
                    print(f"Предупреждение: не удалось загрузить объект {item_dict.get('name', '?')}: {e}")
        
        return items
    except Exception as e:
        raise StorageError(f"Ошибка загрузки: {str(e)}")