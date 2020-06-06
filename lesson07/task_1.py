# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 99
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)


def bubble(arr):
    n = 1
    while n < len(arr):
        flag = 0
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                flag = 1
        if flag == 0:
            break
        n += 1
    return arr


print(bubble(array))

# Из улучшений в цикле for мы берем range(len(arr) - n), а не range(len(arr) - 1) - это уменьшает
# обход нашего массива, исключая уже упорядоченную часть, с каждым витком цикла while.
# Переменная flag отслеживает, были ли обмен элементов во время прохождения по массиву в цикле. Если не был
# то значение меняется на 1 и мы выходим из цикла, т.к. массив уже отсортирован.
