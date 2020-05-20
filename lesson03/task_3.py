# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

import random

SIZE = 20
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


ind_max = -1
for i in range(len(array)):
    if array[i] < 0 and ind_max == -1:
        ind_max = i
    elif 0 > array[i] >= array[ind_max]:
        ind_max = i

if ind_max != -1:
    print(f'Наибольший отрицательный элемент {array[ind_max]} с индексом {ind_max}.')
else:
    print(f'Отрицательных элементов в массиве нет.')




