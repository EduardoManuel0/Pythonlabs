# Импорт класса Atleta из Lab01
import sys
import os

# Garante que conseguimos importar o Product do lab01
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))  # Поднимаем уровень на одну папку вверх

from src.lab01.model import Atleta


class AtletaCollection:
    """Контейнерный класс для хранения и управления коллекцией объектов Atleta."""


    def __init__(self):
        """Инициализация коллекции. Внутри хранится список объектов."""
        self._items = []

    def add(self, item: Atleta):
        """Добавляет объект в коллекцию с проверкой типа и дубликатов."""
        if not isinstance(item, Atleta):
            raise TypeError("Можно добавлять только объекты типа Atleta")
        if self.find_by_name(item.nome):  # Исправлено: nome → name
            raise ValueError(f"Спортсмен с именем '{item.nome}' уже существует в коллекции")  # Исправлено: nome → name
        self._items.append(item)

    def remove(self, item: Atleta) -> bool:
        """Удаляет объект из коллекции. Удаляет первое вхождение."""
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False

    def get_all(self) -> list[Atleta]:
        """Возвращает список всех объектов в коллекции."""
        return self._items.copy()

    def find_by_name(self, name: str) -> Atleta | None:  # Исправлено: nome → name
        """Ищет спортсмена по имени. Возвращает первого найденного."""
        for atleta in self._items:
            if atleta.nome == name:  # Исправлено: nome → name
                return atleta
        return None

    def find_by_sport(self, sport: str) -> list[Atleta]:  # Исправлено: esporte → sport
        """Ищет спортсменов по виду спорта. Возвращает всех подходящих."""
        return [atleta for atleta in self._items if atleta.esporte == sport]  # Исправлено: esporte → sport


    def find_by_age(self, age: int) -> list[Atleta]:  # Исправлено: idade → age
        """Ищет спортсменов по возрасту. Возвращает всех подходящих."""
        return [atleta for atleta in self._items if atleta.idade == age]  # Исправлено: idade → age

    def __len__(self) -> int:
        """Позволяет использовать len(collection)."""
        return len(self._items)

    def __iter__(self):
        """Позволяет итерировать по коллекции: for item in collection."""
        return iter(self._items)

    def __str__(self) -> str:
        """Строковое представление коллекции."""
        return f"AtletaCollection ({len(self)} спортсменов)"

    def __repr__(self) -> str:
        """Техническое представление коллекции."""
        return f"AtletaCollection(items={len(self._items)})"
