"""Сохранение и загрузка объектов ЛР-7 в JSON."""

from __future__ import annotations

import json
import os
from typing import Any

try:
    from .exceptions import StorageError
except ImportError:
    from exceptions import StorageError


def _get_attr(item: Any, public_name: str, protected_name: str | None = None, default: Any = None) -> Any:
    """Безопасно получает атрибут объекта."""
    if hasattr(item, public_name):
        return getattr(item, public_name)
    if protected_name and hasattr(item, protected_name):
        return getattr(item, protected_name)
    return default


def _item_to_dict(item: Any) -> dict[str, Any]:
    """Преобразует объект предметной области в словарь."""
    class_name = type(item).__name__
    result: dict[str, Any] = {
        "__class__": class_name,
        "name": _get_attr(item, "name", "_name", ""),
        "price": _get_attr(item, "price", "_price", 0),
        "producer": _get_attr(item, "producer", None, ""),
        "id": _get_attr(item, "_id", "id", ""),
        "description": _get_attr(item, "description", None, ""),
        "comments": _get_attr(item, "comments", None, {}),
        "mark": _get_attr(item, "mark", "_mark", 3.0),
        "status": _get_attr(item, "_status", None, 0),
    }

    if class_name in {"Product", "Food", "Technic", "Techic"}:
        result["quantity"] = _get_attr(item, "quantity", "_quantity", 0)
        result["cost_price"] = _get_attr(item, "cost_price", "__cost_price__", 1.0)

    if class_name == "Food":
        result["expiration_per"] = _get_attr(item, "expiration_per", "_expiration_days", 1)
        result["calories"] = _get_attr(item, "calories", None, 0)

    if class_name in {"Technic", "Techic"}:
        result["warranty_months"] = _get_attr(item, "warranty_months", "_warranty_months", 0)
        result["power_consumption"] = _get_attr(item, "power_consumption", None, 1.0)

    if class_name == "Estate":
        location = _get_attr(item, "location", "_location", (0.0, 0.0))
        result["location"] = list(location) if isinstance(location, tuple) else location
        result["proportions"] = _get_attr(item, "proportions", "_proportions", 0)
        result["free"] = _get_attr(item, "free", "_free", 1)

    return result


def _dict_to_item(data: dict[str, Any], model_classes: dict[str, type[Any]]) -> Any:
    """Создает объект из словаря."""
    class_name = data.pop("__class__", "Product")
    cls = model_classes.get(class_name)
    if cls is None:
        raise StorageError(f"Неизвестный класс: {class_name}")

    if "location" in data and isinstance(data["location"], list):
        data["location"] = tuple(data["location"])

    try:
        return cls(**data)
    except TypeError:
        if class_name == "Food" and "expiration_per" in data:
            data["expiration_period"] = data.pop("expiration_per")
            return cls(**data)
        if class_name in {"Technic", "Techic"} and "power_consumption" in data:
            data["power"] = data.pop("power_consumption")
            return cls(**data)
        if class_name == "Estate" and "proportions" in data:
            data["area"] = data.pop("proportions")
            return cls(**data)
        raise


def save(collection: list[Any], filepath: str) -> None:
    """Сохраняет коллекцию объектов в JSON-файл."""
    try:
        data = [_item_to_dict(item) for item in collection]
        with open(filepath, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
    except Exception as exc:
        raise StorageError(f"Ошибка сохранения: {exc}") from exc


def load(filepath: str, model_classes: dict[str, type[Any]]) -> list[Any]:
    """Загружает коллекцию объектов из JSON-файла."""
    if not os.path.exists(filepath):
        return []

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            raw_data = json.load(file)

        result: list[Any] = []
        for item_data in raw_data:
            try:
                result.append(_dict_to_item(dict(item_data), model_classes))
            except Exception as exc:
                print(f"Не удалось загрузить объект: {exc}")
        return result
    except Exception as exc:
        raise StorageError(f"Ошибка загрузки: {exc}") from exc
