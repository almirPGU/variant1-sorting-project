from student import create_student


def load_students(filename):
    students = []
    try:
        f = open(filename, encoding='utf-8')
    except FileNotFoundError:
        print("Не удалось открыть файл students.txt")
        return None

    line_num = 0
    for line in f:
        line_num += 1
        parts = line.strip().split(";")
        if len(parts) != 7:
            print(f"Ошибка формата в строке {line_num}")
            return None
        try:
            day = int(parts[2])
            month = int(parts[3])
            year = int(parts[4])
            grade = int(parts[5])
        except ValueError:
            print(f"Ошибка чисел в строке {line_num}")
            return None

        if not (1 <= day <= 31 and 1 <= month <= 12 and 8 <= grade <= 11):
            print(f"Некорректные данные в строке {line_num}")
            return None

        students.append(
            create_student(parts[0], parts[1], day, month, year, grade, parts[6])
        )

    f.close()

    return students
