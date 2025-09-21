# Определяем тип записи студента
StudentRecord = tuple[str, str, float]
def format_record(rec:StudentRecord) -> str:
    fio = rec[0].strip() # Убираем лишние пробелы
    group = rec[1].strip() # Убираем лишние пробелы
    gpa = rec[2] # Значение GPA
# Обрабатываем ФИО
    names = fio.split() # Разделяем строку на части
    surname = names[0] # Фамилия
    initials = [name[0].upper() + '.'for name in names[1:]] # Инициалы (инициалы всех имён)
# Формируем строку результата
    formatted_gpa = f"{gpa:.2f}" # Форматируем GPA с 2 знаками после запятой
    return f"{surname} {' '.join(initials)},гр.{group}, GPA {formatted_gpa}"
# Пример использования
student = ("Eduardo Manuel", "BIVT-25", 4.6)
print(format_record(student)) # "Иванов И.И., гр. BIVT-25, GPA 4.60"