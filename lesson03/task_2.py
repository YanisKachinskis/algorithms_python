# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

i = 0
min_ = max_ = array[0]
for itm in array:
    if min_ >= itm:
        min_ = itm
        ind_min = i
    if max_ <= itm:
        max_ = itm
        ind_max = i
    i = i + 1
array[ind_min], array[ind_max] = array[ind_max], array[ind_min]
print(array)
print(f'Минимальный элемент: {min_}\nМаксимальный элемент: {max_}')
print(f'Индекс минимального элемента: {ind_min}\nИндекс максимального элемента: {ind_max}\n')
