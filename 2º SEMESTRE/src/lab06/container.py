from typing import TypeVar, Generic, Callable, Optional, Protocol

# TypeVars для Generic-коллекции
T = TypeVar('T')
R = TypeVar('R')
D = TypeVar('D', bound='Displayable')
S = TypeVar('S', bound='Scorable')

# Протоколы для структурной типизации
class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

class TypedCollection(Generic[T]):
    """
    Generic-коллекция с поддержкой аннотаций типов.
    Хранит элементы одного типа и предоставляет методы для работы с ними.
    """

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        self._items.remove(item)

    def get_all(self) -> list[T]:
        """Возвращает копию списка всех элементов."""
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит первый элемент, удовлетворяющий условию.
        Возвращает None, если элемент не найден.
        """
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        """
        Фильтрует элементы по условию и возвращает список подходящих.
        """
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> list[R]:
        """
        Применяет функцию преобразования к каждому элементу.
        Возвращает список результатов с потенциально другим типом.
        """
        return [transform(item) for item in self._items]
