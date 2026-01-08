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

    for student in students:
        date = f"{student['day']:02}.{student['month']:02}.{student['year']}"
        print(
            f"{student['surname']:<12}"
            f"{student['name']:<10}"
            f"{date:<15}"
            f"{student['grade_num']}{student['grade_letter']}"
        )

    print("-" * 70)
