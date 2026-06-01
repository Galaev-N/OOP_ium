from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Generic, Iterator, Optional, Protocol, TypeVar, runtime_checkable

# lab06 лежит рядом с lab05, поэтому подключаем прошлую лабораторную через импорт.
# Копировать старые классы сюда не надо, иначе проект превратится в болото. А он и так старается.
CURRENT_DIR = Path(__file__).resolve().parent
LAB05_DIR = CURRENT_DIR.parent / "lab05"
if str(LAB05_DIR) not in sys.path:
    sys.path.insert(0, str(LAB05_DIR))

from new_models import Product, Food, Technic, Estate  # noqa: E402


T = TypeVar("T")
R = TypeVar("R")


@runtime_checkable
class Displayable(Protocol):
    def display(self) -> str:
        ...


@runtime_checkable
class Scorable(Protocol):
    def score(self) -> float:
        ...


D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)


class TypedCollection(Generic[T]):
    """Generic-коллекция с интерфейсом, похожим на ProductCatalog из lab02/lab05."""

    def __init__(self, items: Optional[list[T]] = None, item_type: Optional[type] = None) -> None:
        self._item_type: Optional[type] = item_type
        self._items: list[T] = []

        if items is not None:
            if not isinstance(items, list):
                raise TypeError("Ошибка! Неверный формат каталога")
            for item in items:
                self.add(item)

    @property
    def items(self) -> list[T]:
        return self._items

    def _check_type(self, item: T) -> None:
        if self._item_type is not None and not isinstance(item, self._item_type):
            raise TypeError(
                f"Ошибка! Ожидался объект типа {self._item_type.__name__}, "
                f"получен {type(item).__name__}"
            )

    # Новый нормальный интерфейс
    def add(self, item: T) -> None:
        self._check_type(item)
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> list[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        return [transform(item) for item in self._items]

    # Методы по образу прошлых лаб, потому что традиции надо уважать, даже странные.
    def A(self, obj: T) -> str:
        self.add(obj)
        name = getattr(obj, "name", str(obj))
        return f"Продукт {name} был успешно добавлен!"

    def R(self, obj: T) -> str:
        if obj not in self._items:
            raise ValueError("Такого продукта нет в каталоге")
        self.remove(obj)
        name = getattr(obj, "name", str(obj))
        return f"Продукт {name} был успешно удален!"

    def GAll(self) -> list[T]:
        return self.get_all()

    def FBI(self, id: str) -> Optional[T]:
        for obj in self._items:
            if getattr(obj, "_id", None) == id or getattr(obj, "id", None) == id:
                return obj
        return None

    def RAI(self, index: int) -> T:
        if index < 0 or index >= len(self._items):
            raise IndexError(f"Индекс {index} вне диапазона (0-{len(self._items) - 1})")
        return self._items.pop(index)

    def SBP(self) -> list[T]:
        self._items.sort(key=lambda item: getattr(item, "price", 0))
        return self._items

    def GAva(self) -> "TypedCollection[T]":
        result: TypedCollection[T] = TypedCollection(item_type=self._item_type)
        for item in self._items:
            if hasattr(item, "quantity") and getattr(item, "quantity") > 0:
                result.add(item)
            elif hasattr(item, "free") and getattr(item, "free") in (1, True):
                result.add(item)
        return result

    def sort_by(self, strategy: Callable[[T], object], reverse: bool = False) -> "TypedCollection[T]":
        self._items.sort(key=strategy, reverse=reverse)
        return self

    def filter_by(self, strategy: Callable[[T], bool]) -> "TypedCollection[T]":
        self._items = [item for item in self._items if strategy(item)]
        return self

    def apply(self, strategy: Callable[[T], T]) -> "TypedCollection[T]":
        self._items = [strategy(item) for item in self._items]
        return self

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]
