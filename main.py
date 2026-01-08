from data_io import load_students
from sorting import insertion_sort
from student import print_students, create_student


def add_student(students):
    print("\nДобавление ученика (0 — назад)")

    # Фамилия
    while True:
        surname = input("Фамилия: ")
        if surname == "0":
            return
        if surname.isalpha():
            break
        print("Ошибка: только буквы")

    # Имя
    while True:
        name = input("Имя: ")
        if name == "0":
            return
        if name.isalpha():
            break
        print("Ошибка: только буквы")

    # День
    while True:
        day = input("День рождения (1–31): ")
        if day == "0":
            return
        if day.isdigit() and 1 <= int(day) <= 31:
            day = int(day)
            break
        print("Ошибка: число от 1 до 31")

    # Месяц
    while True:
        month = input("Месяц рождения (1–12): ")
        if month == "0":
            return
        if month.isdigit() and 1 <= int(month) <= 12:
            month = int(month)
            break
        print("Ошибка: число от 1 до 12")

    # Год
    while True:
        year = input("Год рождения: ")
        if year == "0":
            return
        if year.isdigit():
            year = int(year)
            break
        print("Ошибка: введите год числом")

    # Класс
    while True:
        grade = input("Класс (8–11): ")
        if grade == "0":
            return
        if grade.isdigit() and 8 <= int(grade) <= 11:
            grade = int(grade)
            break
        print("Ошибка: класс от 8 до 11")

    # Буква класса
    while True:
        letter = input("Буква класса: ").upper()
        if letter == "0":
            return
        if letter.isalpha() and len(letter) == 1:
            break
        print("Ошибка: одна буква")

    student = {
        "surname": surname,
        "name": name,
        "day": day,
        "month": month,
        "year": year,
        "grade_num": grade,
        "grade_letter": letter
    }

    try:
        with open("students.txt", "a", encoding="utf-8") as f:
            f.write(
                f"{surname};{name};{day};{month};{year};{grade};{letter}\n"
            )
    except OSError:
        print("Ошибка записи в файл")
        return

    students.append(student)
    print("Ученик добавлен и сохранён")


def season_menu(students):
    months = {
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

        if season not in months:
            print("Неизвестное время года")
            continue

        filt = [s for s in students if s["month"] in months[season]]
        res = insertion_sort(filt, lambda s: (s["month"], s["day"], s["surname"]))
        print_students(res)
        return


def parallel_menu(students):
    while True:
        cls = input("\nВведите номер класса (8-11) или 0 для возврата: ")

        if cls == "0":
            return

        if not cls.isdigit():
            print("Нужно ввести число")
            continue

        cls = int(cls)
        if not (8 <= cls <= 11):
            print("Класс должен быть от 8 до 11")
            continue

        filt = [s for s in students if s["grade_num"] == cls]
        if not filt:
            print("В этой параллели нет учеников")
            continue

        res = insertion_sort(filt, lambda s: (s["month"], s["day"], s["surname"]))
        print_students(res)
        return


def main():
    students = load_students("students.txt")
    if students is None:
        return

    if not students:
        print("Файл students.txt пуст. Можно добавить учеников через меню.")

    while True:
        print("Допускается добавление вручную в формате (Ф;И;ДД;ММ;ГГГГ;КЛАСС;БУКВА КЛАССА)")
        print("\nГЛАВНОЕ МЕНЮ")
        print("1 - Полный список учеников")
        print("2 - Именинники по времени года")
        print("3 - Ученики одной параллели")
        print("4 - Добавить ученика")
        print("0 - Выход")

        cmd = input("Ваш выбор: ")

        if cmd == "1":
            res = insertion_sort(
                students,
                lambda s: (s["grade_num"], s["grade_letter"], s["surname"])
            )
            print_students(res)

        elif cmd == "2":
            season_menu(students)

        elif cmd == "3":
            parallel_menu(students)

        elif cmd == "4":
            add_student(students)

        elif cmd == "0":
            print("Работа программы завершена")
            break

        else:
            print("Нет такого пункта меню")


if __name__ == "__main__":
    main()
