from data_io import load_students
from sorting import insertion_sort
from student import print_students


# Добавляет нового ученика через ввод с клавиатуры
# и сохраняет его в файл students.txt
def add_student(students):
    print("\nДобавление ученика (0 — назад)")

    # Ввод фамилии
    while True:
        surname = input("Фамилия: ")
        if surname == "0":
            return
        if surname.isalpha():
            break
        print("Ошибка: только буквы")

    # Ввод имени
    while True:
        name = input("Имя: ")
        if name == "0":
            return
        if name.isalpha():
            break
        print("Ошибка: только буквы")

    # Ввод дня рождения
    while True:
        day_input = input("День рождения (1–31): ")
        if day_input == "0":
            return
        if day_input.isdigit() and 1 <= int(day_input) <= 31:
            day = int(day_input)
            break
        print("Ошибка: число от 1 до 31")

    # Ввод месяца рождения
    while True:
        month_input = input("Месяц рождения (1–12): ")
        if month_input == "0":
            return
        if month_input.isdigit() and 1 <= int(month_input) <= 12:
            month = int(month_input)
            break
        print("Ошибка: число от 1 до 12")

    # Ввод года рождения
    while True:
        year_input = input("Год рождения: ")
        if year_input == "0":
            return
        if year_input.isdigit():
            year = int(year_input)
            break
        print("Ошибка: введите год числом")

    # Ввод номера класса
    while True:
        class_input = input("Класс (8–11): ")
        if class_input == "0":
            return
        if class_input.isdigit() and 8 <= int(class_input) <= 11:
            grade_num = int(class_input)
            break
        print("Ошибка: класс от 8 до 11")

    # Ввод буквы класса
    while True:
        grade_letter = input("Буква класса: ").upper()
        if grade_letter == "0":
            return
        if grade_letter.isalpha() and len(grade_letter) == 1:
            break
        print("Ошибка: одна буква")

    # Формируем словарь с данными ученика
    student = {
        "surname": surname,
        "name": name,
        "day": day,
        "month": month,
        "year": year,
        "grade_num": grade_num,
        "grade_letter": grade_letter
    }

    try:
        # Записываем нового ученика в файл
        with open("students.txt", "a", encoding="utf-8") as file:
            file.write(
                f"{surname};{name};{day};{month};{year};{grade_num};{grade_letter}\n"
            )
    except OSError:
        # Обработка ошибки записи в файл
        print("Ошибка записи в файл")
        return

    # Добавляем ученика в список в памяти
    students.append(student)
    print("Ученик добавлен и сохранён")


# Меню вывода учеников, родившихся в указанное время года
def season_menu(students):
    # Соответствие времени года и номеров месяцев
    seasons = {
        "зима": [12, 1, 2],
        "весна": [3, 4, 5],
        "лето": [6, 7, 8],
        "осень": [9, 10, 11]
    }

    while True:
        season = input(
            "\nВведите время года (зима/весна/лето/осень) или 0 для возврата: "
        ).lower()

        if season == "0":
            return

        if season not in seasons:
            print("Неизвестное время года")
            continue

        # Отбираем учеников по месяцу рождения
        filtered_students = [
            student for student in students if student["month"] in seasons[season]
        ]

        # Сортируем по месяцу, дню и фамилии
        sorted_students = insertion_sort(
            filtered_students,
            lambda student: (student["month"], student["day"], student["surname"])
        )

        print_students(sorted_students)
        return


# Меню вывода учеников одной параллели
def parallel_menu(students):
    while True:
        class_input = input("\nВведите номер класса (8–11) или 0 для возврата: ")

        if class_input == "0":
            return

        if not class_input.isdigit():
            print("Нужно ввести число")
            continue

        class_num = int(class_input)
        if not (8 <= class_num <= 11):
            print("Класс должен быть от 8 до 11")
            continue

        # Отбираем учеников указанного класса
        filtered_students = [
            student for student in students if student["grade_num"] == class_num
        ]

        if not filtered_students:
            print("В этой параллели нет учеников")
            continue

        # Сортируем по дате рождения и фамилии
        sorted_students = insertion_sort(
            filtered_students,
            lambda student: (student["month"], student["day"], student["surname"])
        )

        print_students(sorted_students)
        return


def main():
    # Загружаем данные из файла
    students = load_students("students.txt")
    if students is None:
        return

    # Сообщение, если файл пуст
    if not students:
        print("Файл students.txt пуст. Можно добавить учеников через меню.")

    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1 - Полный список учеников")
        print("2 - Именинники по времени года")
        print("3 - Ученики одной параллели")
        print("4 - Добавить ученика")
        print("0 - Выход")

        command = input("Ваш выбор: ")

        if command == "1":
            # Сортировка полного списка по классу и фамилии
            sorted_students = insertion_sort(
                students,
                lambda student: (
                    student["grade_num"],
                    student["grade_letter"],
                    student["surname"]
                )
            )
            print_students(sorted_students)

        elif command == "2":
            season_menu(students)

        elif command == "3":
            parallel_menu(students)

        elif command == "4":
            add_student(students)

        elif command == "0":
            print("Работа программы завершена")
            break

        else:
            print("Нет такого пункта меню")


# Точка входа в программу
if __name__ == "__main__":
    main()
