# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

import sys

FIRST_LETTER = 96
a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')

# 1-е решение

print('Решение №1')
memory1 = [FIRST_LETTER, a, b]
first_number = ord(a) - FIRST_LETTER
memory1.append(first_number)
second_number = ord(b) - FIRST_LETTER
memory1.append(second_number)
dif_number = abs(second_number - first_number) - 1
memory1.append(dif_number)
print(f'Номер первой буквы: {first_number}')
print(f'Номер второй буквы: {second_number}')
print(f'Число букв между ними: {dif_number}')
# print(memory1)

# 2-е решение

print('Решение №2')
dct1 = {}
dct2 = {}
memory2 = [FIRST_LETTER, a, b]
n = FIRST_LETTER
i = 1
while chr(n) != a:
    dct1.update({chr(n + 1): i})
    n += 1
    i += 1
memory2.append(n)
memory2.append(i)
memory2.append(dct1)
print(f'Номер буквы {a} - {dct1[a]}')
# print(dct1)

n = FIRST_LETTER
i = 1
while chr(n) != b:
    dct2.update({chr(n + 1): i})
    n += 1
    i += 1
print(f'Номер буквы {b} - {dct2[b]}')
# print(dct2)
memory2.append(dct2)
memory2.append(n)
memory2.append(i)

diff = abs(dct2[b] - dct1[a]) - 1
memory2.append(diff)
print(f'Между ними {diff} символа(ов).')

# Решение №3

print('Решение №3')
memory3 = [FIRST_LETTER, a, b]
alphabet = 'abcdefghigklmnopqrstuvwxyz'
memory3.append(alphabet)
j = 1
for i in alphabet:
    if i == a:
        first = j
        break
    j += 1
memory3.append(j)
k = 1
for i in alphabet:
    if b == i:
        second = k
        break
    k += 1
memory3.append(k)
difference = abs(second - first) - 1
memory3.append(difference)
print(f'Номер первой буквы: {first}')
print(f'Номер второй буквы: {second}')
print(f'Число букв между ними: {difference}')


def show(object):
    size = sys.getsizeof(object)
    if hasattr(object, '__iter__'):
        if hasattr(object, 'items'):
            for key, value in object.items():
                size += show(key)
                size += show(value)
        elif not isinstance(object, str):
            for item in object:
                size += show(item)
    return size


print('*' * 50)
print(f'Память затраченная на работу первого варианта: {show(memory1) - sys.getsizeof(memory1)}')
print('*' * 50)
print(f'Память затраченная на работу второго варианта: {show(memory2) - sys.getsizeof(memory2)}')
print('*' * 50)
print(f'Память затраченная на работу третьего варианта: {show(memory3) - sys.getsizeof(memory3)}')

# Win10 Pro 1903, 64-bit
# Замер проводился для букв "e" и "r".
# Очевидно, что меньше всего памяти испорльзуется в первом варианте решения, где не задействованны такие типы данных,
# как словари и массивы, а используются только переменные типа int и str с небольшими значениями.
# Память затраченная на работу первого варианта: 108
# **************************************************
# Память затраченная на работу второго варианта: 1528
# **************************************************
# Память затраченная на работу третьего варианта: 159