# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 50
MIN_ITEM = 1
MAX_ITEM = 10
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
print(sorted(array))
max_count = 1
for i in range(len(array) - 1):
    count = 1
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            count += 1
    if count > max_count:
        max_count = count
        numb = array[i]
print(f'Число {numb} повторяется {max_count} раз(а).')
