from typing import TypeVar, Generic, Iterator

T = TypeVar('T')

class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: list[T] = []
    
    @property
    def items(self) -> list:
        return self._items

    def A(self, obj: T) -> str: # Add
        self._items.append(obj)
        return f'Продукт {obj.name} был успешно добавлен!'

    def R(self, obj: T) -> str: # Remove
        if obj in self._items: self._items.remove(obj)
        else: raise ValueError(f'Такого продукта нет в каталоге')
        return f'Продукт {obj.name} был успешно Удален!'

    def GAll(self) -> str: #Get All
        return f'Вот содержимое коллекции:\n{self._items}'
    
    def FBI(self, id: str) -> T: # Find By Id
        for obj in self._items:
            if obj._id == id:
                return obj
    
    def __len__(self) -> int: # Это было проще, чем я думал
        return len(self._items)

    def __iter__(self) -> Iterator:
        # Возвращаем итератор от нашего списка
        return iter(self._items)
    
    def __getitem__(self, index: str) -> T: # Позволяет обращаться к элементам множества по индексу
        return self._items[index]
    
    def RAI(self, index: str) -> None: # Remove At Index
        if index < 0 or index >= len(self._items):
            raise IndexError(f'Индекс {index} вне диапазона (0-{len(self._items)-1})')
        return self._items.pop(index)
    
    
    def GAva(self) -> TypedCollection(Generic[T]): # Get Avalible
        Available_cat = TypedCollection(Generic[T])
    
        for item in self._items:
            # Для Food и Techic проверяем quantity
                if hasattr(item, 'quantity') and not hasattr(item, 'free'):
                    if item.quantity != 0:
                        Available_cat.A(item)
                        # Для Estate проверяем free
                elif hasattr(item, 'free'):
                    if item.free == 1:
                        Available_cat.A(item)
            # Для обычного Product
                elif hasattr(item, 'quantity'):
                    if item.quantity != 0:
                        Available_cat.A(item)
    
        return Available_cat
    
    def sort_by(self, s_s: function, reverse=False) -> TypedCollection(Generic[T]):
        self._items.sort(key=s_s, reverse=reverse)
        return self
    
    def filter_by(self, f_s: function) -> TypedCollection(Generic[T]):
        self._items = [i for i in self._items if f_s(i)] 
        return self
    
    def apply(self, t_s: function) -> TypedCollection(Generic[T]):
        self._items = [t_s(item) for item in self._items]
        return self