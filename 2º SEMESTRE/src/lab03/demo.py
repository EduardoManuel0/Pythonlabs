from base import AtletaManager
from models import AtletaPro, AtletaAmador

def run_demo():
    print("="*70)
    print(" ДЕМОНСТРАЦИЯ ЛР-03, 04, 05: НАСЛЕДОВАНИЕ И ПОЛИМОРФИЗМ")
    print("="*70)

    # 1. Инициализация менеджера
    manager = AtletaManager()

    # 2. Создание объектов разных типов
    pro1 = AtletaPro("Cristiano Ronaldo", 39, 85.0, 1.87, "futebol", "Nike", 1)
    pro2 = AtletaPro("Lionel Messi", 36, 72.0, 1.70, "futebol", "Adidas", 2)
    amador = AtletaAmador("Иван Иванов", 25, 75.0, 1.80, "natacao", "Спартак", 12)

    manager.add(pro1)
    manager.add(pro2)
    manager.add(amador)

    # 3. Демонстрация полиморфизма (Задание 5: вызов без IF)
    print("\n--- СЦЕНАРИЙ 1: ПОЛИМОРФНЫЙ РАСЧЕТ БОНУСОВ ---")
    for atleta in manager:
        # Вызываем один и тот же метод для разных классов
        print(f"Спортсмен: {atleta.nome:20} | Тип: {type(atleta).__name__:15} | Бонус: ${atleta.calcular_bonus()}")

    # 4. Фильтрация по типу (Задание 5)
    print("\n--- СЦЕНАРИЙ 2: ФИЛЬТРАЦИЯ ТОЛЬКО ПРОФЕССИОНАЛОВ ---")
    pros = manager.get_only_pros()
    for p in pros:
        print(f"Найден профи: {p.nome} (Рейтинг: {p.ranking})")

    # 5. Проверка isinstance (Задание 4)
    print("\n--- СЦЕНАРИЙ 3: ПРОВЕРКА ТИПОВ ЧЕРЕЗ ISINSTANCE ---")
    for atleta in manager:
        status = "Профессионал" if isinstance(atleta, AtletaPro) else "Любитель"
        print(f"Объект {atleta.nome} является типом {status}")

    # 6. Полный вывод информации
    print("\n--- СЦЕНАРИЙ 4: ПОЛНАЯ ИНФОРМАЦИЯ ОБ ОБЪЕКТАХ ---")
    print(pro1)
    print(amador)

    print("="*70)
    print(" ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("="*70)

if __name__ == "__main__":
    run_demo()
