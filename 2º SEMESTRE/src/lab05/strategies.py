"""
Модуль стратегий для обработки объектов Atleta
"""

def by_name(atleta):
    """Стратегия сортировки по имени"""
    return atleta.nome

def by_age(atleta):
    """Стратегия сортировки по возрасту"""
    return atleta.idade

def by_weight_height(atleta):
    """Стратегия по весу и росту одновременно"""
    return (atleta.peso, atleta.altura)

def make_age_filter(min_age):
    """Фабрика функций для фильтрации по возрасту"""
    def filter_fn(atleta):
        return atleta.idade >= min_age
    return filter_fn

class IntensityBonusStrategy:
    """Паттерн Стратегия через callable-объект для расчета бонуса энергии"""
    def __init__(self, multiplier):
        self.multiplier = multiplier
        
    def __call__(self, atleta):
        # Эмуляция обновления данных или расчета
        return f"{atleta.nome}: Бонус {atleta.peso * self.multiplier:.2f}"
