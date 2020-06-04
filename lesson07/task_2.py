# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными
# числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 49.99
array = [round(random.uniform(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]
print(array)


def merger(arr):
    if len(arr) <= 1:
        return arr
    new_array = []
    middle = len(arr) // 2
    half1 = merger(arr[:middle])
    half2 = merger(arr[middle:])
    i = 0
    j = 0
    k = 0
    while k < (len(half1) + len(half2)):
        if i < len(half1) and j < len(half2):
            if half1[i] <= half2[j]:
                new_array.append(half1[i])
                i += 1
            else:
                new_array.append(half2[j])
                j += 1
        elif i == len(half1):
            new_array.append(half2[j])
            j += 1
        elif j == len(half2):
            new_array.append(half1[i])
            i += 1
        k += 1
    return new_array


print(merger(array))
