import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from collection import FunctionalAtletaCollection
from src.lab04.models import ProfessionalAthlete, AmateurAthlete
import strategies

def run_demo():
    print("="*70)
    print(" ДЕМОНСТРАЦИЯ ЛР-05: ФУНКЦИОНАЛЬНОЕ ПРОГРАММИРОВАНИЕ И СТРАТЕГИИ")
    print("="*70)

    # Создание данных
    col = FunctionalAtletaCollection()
    col.add(ProfessionalAthlete("Cristiano", 39, 85.0, 1.87, "futebol", "Nike", 1))
    col.add(ProfessionalAthlete("Messi", 36, 72.0, 1.70, "futebol", "Adidas", 2))
    col.add(AmateurAthlete("Ivan", 20, 70.0, 1.80, "natacao", "Spartak", 10))
    col.add(AmateurAthlete("Anna", 22, 55.0, 1.65, "atletismo", "Zenit", 15))
    col.add(AmateurAthlete("Petr", 30, 90.0, 1.85, "boxe", "Dynamo", 5))

    # Сценарий 1: Цепочка операций (Filter -> Sort -> Map/Apply)
    print("\n--- СЦЕНАРИЙ 1: ЦЕПОЧКА ОПЕРАЦИЙ (Возраст >= 25 + Сортировка по имени) ---")
    age_filter = strategies.make_age_filter(25)
    
    (col.filter_by(age_filter)
        .sort_by(strategies.by_name))
    
    for a in col:
        print(f"  [Результат] {a.nome}, возраст: {a.idade}")

    # Сценарий 2: Использование Lambda и Map
    print("\n--- СЦЕНАРИЙ 2: ПРЕОБРАЗОВАНИЕ (MAP + LAMBDA) ---")
    names_upper = list(map(lambda x: x.nome.upper(), col.get_all()))
    print(f"  Имена в верхнем регистре: {', '.join(names_upper)}")

    # Сценарий 3: Callable-объект как стратегия
    print("\n--- СЦЕНАРИЙ 3: CALLABLE-ОБЪЕКТ (Бонусная стратегия) ---")
    bonus_strat = strategies.IntensityBonusStrategy(0.1)
    bonuses = col.apply(bonus_strat)
    for b in bonuses:
        print(f"  {b}")

    print("\n" + "="*70)
    print(" ПРОЕКТ ЗАВЕРШЕН (ЛР 1-5)")
    print("="*70)

if __name__ == "__main__":
    run_demo()
