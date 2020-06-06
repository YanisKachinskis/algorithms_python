# 3.  Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
# которые не меньше медианы, в другой — не больше медианы.

import random

SIZE = 9
MIN_ITEM = 0
MAX_ITEM = 50
array = [round(random.randint(MIN_ITEM, MAX_ITEM), 2) for _ in range(SIZE)]


# Решение без сортировки, но работает на для всех массивов. Не работает в некоторых случаях, когда в массиве несколько
# одинаковых элементов

def mediana(arr):
    for i in range(len(arr)):
        n = m = k = 0
        for j in range(len(arr)):
            if arr[j] != arr[i]:
                if arr[j] > arr[i]:
                    n += 1  # n - счетчик больших значений
                else:
                    m += 1  # m - счетчик меньших значений
        if n == m:
            return arr[i]


arr1 = [27, 25, 8, 0, 5, 31, 6, 10, 21]
# [0, 5, 6, 8, 10, 21, 25, 27, 31]

print(arr1)
print(f'Медиана данного массива - {mediana(arr1)}')
print('*' * 50)
print(array)


# Поэтому сделал Гномью сортировку
def dwarf(arr):
    i = 1
    while i < len(arr):
        if arr[i - 1] <= arr[i]:
            i += 1
        else:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            if i > 1:
                i -= 1
    return arr


d = dwarf(array)
med = d[len(d) // 2]
print(d)
print(f'Медиана данного массива - {med}')
