from student import create_student


# Загружает список учеников из текстового файла
def load_students(filename):
    students = []

    try:
        with open(filename, encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                fields = line.strip().split(";")

                # Проверка формата строки (ровно 7 полей)
                if len(fields) != 7:
                    print(f"Ошибка формата в строке {line_number}")
                    return None

                # Проверка фамилии и имени
                if not fields[0].isalpha() or not fields[1].isalpha():
                    print(f"Ошибка имени или фамилии в строке {line_number}")
                    return None

                try:
                    day = int(fields[2])
                    month = int(fields[3])
                    year = int(fields[4])
                    grade_num = int(fields[5])
                except ValueError:
                    print(f"Ошибка числовых данных в строке {line_number}")
                    return None

                # Проверка диапазонов
                if not (1 <= day <= 31 and 1 <= month <= 12 and 8 <= grade_num <= 11):
                    print(f"Некорректные данные в строке {line_number}")
                    return None

                students.append(
                    create_student(
                        fields[0], fields[1],
                        day, month, year,
                        grade_num, fields[6]
                    )
                )

    except FileNotFoundError:
        print(f"Не удалось открыть файл {filename}")
        return None

    return students
