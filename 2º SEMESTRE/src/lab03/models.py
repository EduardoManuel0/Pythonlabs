import sys
import os

# Подключение путей для импорта из предыдущих лабораторных
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.lab01.model import Atleta

class AtletaPro(Atleta):
    """Профессиональный спортсмен (ЛР 3-5)"""
    
    def __init__(self, nome, idade, peso, altura, esporte, patrocinador, ranking):
        # Использование super() для вызова конструктора базового класса
        super().__init__(nome, idade, peso, altura, esporte)
        self.patrocinador = patrocinador
        self.ranking = ranking

    def calcular_bonus(self):
        """Полиморфный метод: расчет бонуса на основе рейтинга."""
        return round(100000 / self.ranking, 2) if self.ranking > 0 else 0.0

    def __str__(self):
        """Переопределение метода вывода."""
        info = super().__str__()
        return (f"{info}СТАТУС: Профессионал\n"
                f"РЕЙТИНГ: {self.ranking}\n"
                f"СПОНСОР: {self.patrocinador}\n"
                f"БОНУС: ${self.calcular_bonus()}\n")


class AtletaAmador(Atleta):
    """Спортсмен-любитель (ЛР 3-5)"""
    
    def __init__(self, nome, idade, peso, altura, esporte, клуб, часы_тренировок):
        super().__init__(nome, idade, peso, altura, esporte)
        self.клуб = клуб
        self.часы_тренировок = часы_тренировок

    def calcular_bonus(self):
        """Полиморфный метод: любители не получают денежных бонусов."""
        return 0.0

    def __str__(self):
        info = super().__str__()
        return (f"{info}СТАТУС: Любитель\n"
                f"КЛУБ: {self.клуб}\n"
                f"ТРЕНИРОВКИ: {self.часы_тренировок} ч/нед\n")
