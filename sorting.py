# сортировка вставками

def insertion_sort(arr, key):
    temp = arr[:]
    for i in range(1, len(temp)):
        x = temp[i]
        j = i - 1
        while j >= 0 and key(temp[j]) > key(x):
            temp[j + 1] = temp[j]
            j -= 1
        temp[j + 1] = x
    return temp
