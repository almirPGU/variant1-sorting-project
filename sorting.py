# Сортировка вставками
def insertion_sort(students, key):
    # Копия списка, чтобы не изменять исходные данные
    sorted_students = students[:]

    for index in range(1, len(sorted_students)):
        # Текущий элемент, который нужно вставить на правильное место
        current_student = sorted_students[index]

        # Индекс для сравнения с предыдущими элементами
        previous_index = index - 1

        # Сдвигаем элементы, которые больше текущего
        while (
            previous_index >= 0
            and key(sorted_students[previous_index]) > key(current_student)
        ):
            sorted_students[previous_index + 1] = sorted_students[previous_index]
            previous_index -= 1

        # Вставляем элемент на найденную позицию
        sorted_students[previous_index + 1] = current_student

    return sorted_students
