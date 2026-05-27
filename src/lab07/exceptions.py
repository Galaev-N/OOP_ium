class ItemNotFoundError(Exception):
    def __init__(self, message: str = "Объект не найден в коллекции"):
        self.message = message
        super().__init__(self.message)


class DuplicateItemError(Exception):
    def __init__(self, item_id: str = ""):
        self.item_id = item_id
        message = f"Объект с идентификатором '{item_id}' уже существует"
        super().__init__(message)


class InvalidInputError(Exception):
    def __init__(self, message: str = "Некорректный ввод"):
        self.message = message
        super().__init__(self.message)


class StorageError(Exception):
    def __init__(self, message: str = "Ошибка при работе с файлом"):
        self.message = message
        super().__init__(self.message)