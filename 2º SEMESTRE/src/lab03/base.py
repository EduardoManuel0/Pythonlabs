import sys
import os

# Подключение путей для импорта из предыдущих лабораторных
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab02.collection import AtletaCollection

class AtletaManager(AtletaCollection):
    """
    Класс для управления иерархией спортсменов.
    Реализует фильтрацию по типам (Требование ЛР-5).
    """
    
    def get_only_pros(self):
        """Возвращает только профессиональных спортсменов."""
        from models import AtletaPro
        return [item for item in self._items if isinstance(item, AtletaPro)]

    def get_only_amateurs(self):
        """Возвращает только спортсменов-любителей."""
        from models import AtletaAmador
        return [item for item in self._items if isinstance(item, AtletaAmador)]
