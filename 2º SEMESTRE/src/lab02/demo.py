# Импорт классов из предыдущих модулей
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))


from src.lab01.model import Atleta
from collection import AtletaCollection

def run():
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ЛР-4: КОЛЛЕКЦИЯ ОБЪЕКТОВ ATHLETA (с переиспользованием model.py из Lab01)")
    print("=" * 60)

    # Создание коллекции
    colecao = AtletaCollection()
    print(f"Создана коллекция: {colecao}")

    # Создание нескольких объектов Atleta — используем класс из Lab01
    #atleta1 = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
    #atleta2 = Atleta("Maria Santos", 22, 62.3, 1.68, "atletismo")
    atleta3 = Atleta("Pedro Costa", 28, 85.0, 1.85, "basquete")

    atleta1 = Atleta("João Silva", 25, 75.5, 1.80, "natacao")
    atleta2 = Atleta("Maria Santos", 22, 62.3, 1.68, "atletismo")
    
    print("\n--- ШАГ 1: ДОБАВЛЕНИЕ ОБЪЕКТОВ В КОЛЛЕКЦИЮ ---")
    colecao.add(atleta1)
    colecao.add(atleta2)
    #colecao.add(atleta3)
    print("Три спортсмена успешно добавлены в коллекцию")

    # Вывод всех элементов
    print("\n--- ШАГ 2: ВЫВОД ВСЕХ ЭЛЕМЕНТОВ КОЛЛЕКЦИИ ---")
    todos = colecao.get_all()
    for i, atleta in enumerate(todos, 1):
        print(f"{i}. {atleta}")

    print(f"\nВсего в коллекции: {len(colecao)} спортсменов")

    # Поиск элемента
    print("\n--- ШАГ 3: ПОИСК ЭЛЕМЕНТОВ ---")
    busca_joao = colecao.find_by_name("João Silva")
    if busca_joao:
        print(f"Найден спортсмен: {busca_joao}")
    corredores = colecao.find_by_sport("atletismo")
    print(f"Найдено спортсменов по 'atletismo': {len(corredores)}")
    jovens = colecao.find_by_age(22)
    print(f"Найдено спортсменов возрастом 22 года: {len(jovens)}")

    # Использование len()
    print("\n--- ШАГ 4: ИСПОЛЬЗОВАНИЕ len() ---")
    print(f"Всего спортсменов в коллекции: {len(colecao)}")

    # Использование for
    print("\n--- ШАГ 5: ИСПОЛЬЗОВАНИЕ for ---")
    print("Перебор всех спортсменов:")
    for atleta in colecao:
        print(f"  - {atleta.nome}")

    # Проверка валидации типов и дубликатов
    print("\n--- ШАГ 6: ПРОВЕРКА ВАЛИДАЦИИ ТИПОВ И ДУБЛИКАТОВ ---")
    try:
        colecao.add("Это не спортсмен!")
    except TypeError as e:
        print(f"Поймано исключение (неверный тип): {e}")
    try:
        colecao.add(Atleta("João Silva", 30, 80.0, 1.82, "futebol"))
    except ValueError as e:
        print(f"Поймано исключение (дубликат): {e}")

    # Финальный вывод коллекции
    print("\n--- ШАГ 7: ФИНАЛЬНОЕ СОСТОЯНИЕ КОЛЛЕКЦИИ ---")
    print(f"Всего спортсменов после всех операций: {len(colecao)}")
    print("Список всех спортсменов:")
    for i, atleta in enumerate(colecao.get_all(), 1):
        print(f"{i}. {atleta.nome}")

    print("\n" + "=" * 60)
    print("ДЕМОНСТРАЦИЯ ЗАВЕРШЕНА")
    print("=" * 60)

if __name__ == "__main__":
    run()
