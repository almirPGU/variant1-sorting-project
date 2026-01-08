# Создаёт и возвращает словарь с данными одного ученика
def create_student(surname, name, day, month, year, grade_num, grade_letter):
    return {
        "surname": surname,
        "name": name,
        "day": day,
        "month": month,
        "year": year,
        "grade_num": grade_num,
        "grade_letter": grade_letter
    }


# Выводит список учеников в виде таблицы
def print_students(students):
    print("-" * 70)
    print(f"{'Фамилия':<12}{'Имя':<10}{'Дата рождения':<15}{'Класс'}")
    print("-" * 70)
    for s in students:
        # Формируем дату в формате ДД.ММ.ГГГГ
        date = f"{s['day']:02}.{s['month']:02}.{s['year']}"
        # Вывод одной строки таблицы
        print(f"{s['surname']:<12}{s['name']:<10}{date:<15}{s['grade_num']}{s['grade_letter']}")
    print("-" * 70)
