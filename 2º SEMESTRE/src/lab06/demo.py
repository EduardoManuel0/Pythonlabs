# demo.py — демонстрация работы TypedCollection
from container import TypedCollection, Displayable, Scorable

# Классы для демонстрации (упрощённые версии сущностей из ЛР-1 и ЛР-3)
class Athlete:
    def __init__(self, name: str, weight: float, record: float) -> None:
        self.name: str = name
        self.weight: float = weight
        self.record: float = record

    def display(self) -> str:
        return f"Athlete: {self.name}, Record: {self.record}"

    def score(self) -> float:
        return self.record

class Workout:
    def __init__(self, duration: int, intensity: float) -> None:
        self.duration: int = duration
        self.intensity: float = intensity

    def display(self) -> str:
        return f"Workout: {self.duration} min, Intensity: {self.intensity}"

    def score(self) -> float:
        return self.duration * self.intensity

def main() -> None:
    print("=== Демонстрация TypedCollection ===")

    # Сценарий 1: базовая работа с коллекцией
    print("\n1. Базовая коллекция Athlete:")
    athlete_collection = TypedCollection[Athlete]()
    athlete1 = Athlete("John", 75.0, 10.5)
    athlete2 = Athlete("Alice", 68.0, 9.8)
    athlete_collection.add(athlete1)
    athlete_collection.add(athlete2)
    for athlete in athlete_collection.get_all():
        print(athlete.display())

    # Сценарий 2: использование методов find, filter, map
    print("\n2. Использование методов find/filter/map:")
    # find
    found = athlete_collection.find(lambda a: a.record > 10)
    print(f"Найден атлет с рекордом > 10: {found.name if found else 'Не найден'}")
    not_found = athlete_collection.find(lambda a: a.record > 20)
    print(f"Атлет с рекордом > 20: {'Найден' if not_found else 'Не найден'}")

    # filter
    fast_athletes = athlete_collection.filter(lambda a: a.record < 10)
    print(f"Атлеты с рекордом < 10: {[a.name for a in fast_athletes]}")

    # map — меняем тип результата
    names = athlete_collection.map(lambda a: a.name)
    records = athlete_collection.map(lambda a: a.record * 2)  # удваиваем рекорды
    print(f"Имена атлетов: {names}")
    print(f"Удвоенные рекорды: {records}")

    # Сценарий 3: TypedCollection с протоколом Displayable
    print("\n3. Коллекция с протоколом Displayable:")
    displayable_collection = TypedCollection[Displayable]()
    workout = Workout(60, 0.8)
    displayable_collection.add(athlete1)
    displayable_collection.add(workout)
    for item in displayable_collection.get_all():
        print(item.display())  # безопасно вызываем display()

    # Сценарий 4: TypedCollection с протоколом Scorable
    print("\n4. Коллекция с протоколом Scorable:")
    scorable_collection = TypedCollection[Scorable]()
    scorable_collection.add(athlete1)
    scorable_collection.add(workout)
    scores = scorable_collection.map(lambda s: s.score())
    print(f"Оценки объектов: {scores}")

if __name__ == "__main__":
    main()
