import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from models import ProfessionalAthlete, AmateurAthlete
from interfaces import Printable, Rewardable
from src.lab03.base import AtletaManager

def print_interface_info(items: list[Printable]):
    """Универсальная функция, работающая через интерфейс (Задание 4)."""
    for item in items:
        # Полиморфизм без условий: просто вызываем метод интерфейса
        print(f"  > {item.to_short_string()}")

def run_demo():
    print("="*70)
    print(" ДЕМОНСТРАЦИЯ ЛР-04: ИНТЕРФЕЙСЫ И АБСТРАКТНЫЕ КЛАССЫ (ABC)")
    print("="*70)

    # 1. Создание коллекции
    manager = AtletaManager()

    # 2. Создание объектов (Задание 3-5)
    p1 = ProfessionalAthlete("Cristiano Ronaldo", 39, 85.0, 1.87, "futebol", "Nike", 1)
    a1 = AmateurAthlete("Иван Иванов", 25, 75.0, 1.80, "natacao", "Спартак", 10)
    
    manager.add(p1)
    manager.add(a1)

    # 3. Работа через интерфейс Printable
    print("\n--- СЦЕНАРИЙ 1: ВЫВОД ЧЕРЕЗ ИНТЕРФЕЙС PRINTABLE ---")
    # Приводим к списку и передаем в универсальную функцию
    print_interface_info(manager.get_all())

    # 4. Работа через интерфейс Rewardable
    print("\n--- СЦЕНАРИЙ 2: ИНФОРМАЦИЯ О НАГРАДАХ (ПОЛИМОРФИЗМ) ---")
    for obj in manager:
        if isinstance(obj, Rewardable):
            print(f"Спортсмен: {obj.nome:20} | {obj.get_reward_info()}")

    # 5. Фильтрация коллекции по интерфейсу (Задание 5)
    print("\n--- СЦЕНАРИЙ 3: ФИЛЬТРАЦИЯ ПО ИНТЕРФЕЙСУ ---")
    rewardables = [item for item in manager if isinstance(item, Rewardable)]
    print(f"Найдено объектов с интерфейсом Rewardable: {len(rewardables)}")

    # 6. Проверка реализации нескольких интерфейсов (Задание 4)
    print("\n--- СЦЕНАРИЙ 4: ПРОВЕРКА МНОЖЕСТВЕННОЙ РЕАЛИЗАЦИИ ---")
    test_obj = p1
    print(f"Объект: {test_obj.nome}")
    print(f"  - Реализует Printable: {isinstance(test_obj, Printable)}")
    print(f"  - Реализует Rewardable: {isinstance(test_obj, Rewardable)}")

    print("\n" + "="*70)
    print(" ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("="*70)

if __name__ == "__main__":
    run_demo()
