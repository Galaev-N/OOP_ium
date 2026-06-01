"""Собственные исключения для ЛР-7."""


class ItemNotFoundError(Exception):
    """Объект не найден в коллекции."""


class DuplicateItemError(Exception):
    """Объект с таким идентификатором уже существует."""

    def __init__(self, item_id: str) -> None:
        """Создает ошибку дубликата по ID."""
        super().__init__(f"Объект с ID '{item_id}' уже существует")


class InvalidInputError(Exception):
    """Некорректный пользовательский ввод."""


class StorageError(Exception):
    """Ошибка сохранения или загрузки данных."""
