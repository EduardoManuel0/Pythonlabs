import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab02.collection import AtletaCollection

class FunctionalAtletaCollection(AtletaCollection):
    """Расширенная коллекция с поддержкой функционального стиля (ЛР-5)"""

    def sort_by(self, key_func):
        """Сортировка коллекции по заданной функции"""
        self._items.sort(key=key_func)
        return self  # Для цепочки вызовов

    def filter_by(self, predicate):
        """Фильтрация коллекции по предикату"""
        self._items = list(filter(predicate, self._items))
        return self

    def apply(self, func):
        """Применение функции ко всем элементам (аналог map, но меняет состояние)"""
        # Используем map для демонстрации, хотя в реальности можно просто циклом
        results = list(map(func, self._items))
        return results # Возвращаем результаты обработки
