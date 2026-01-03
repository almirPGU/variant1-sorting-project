# сортировка вставками

def insertion_sort(arr, key):
    res = arr[:]  # копия списка, чтобы не менять исходный

    for i in range(1, len(res)):
        # сохраняем текущий элемент
        new_elem = res[i]

        # начинаем сравнение с предыдущего элемента
        j = i - 1

        # сдвигаем элементы, которые больше new_elem
        while j >= 0 and key(res[j]) > key(new_elem):
            res[j + 1] = res[j]
            j -= 1

        # вставляем элемент на нужное место
        res[j + 1] = new_elem

    return res
