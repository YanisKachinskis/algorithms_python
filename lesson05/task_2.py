# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как коллекция, элементы которой — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их
# как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
# произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque


def count_pattern(i, first, second, index, sum_):
    while i < len(first):
        a = int(first[i], 16)
        b = int(second[i], 16)
        if a + b > 15:
            temp_sum = hex(a + b - 16 + index)
            index = 1
        else:
            temp_sum = hex(a + b + index)
            index = 0
        sum_.appendleft(temp_sum[2:].upper())
        i += 1
    return i, index, sum_


first = deque(input('Введите первое HEX число: '))
second = deque(input('Введите второе HEX число: '))
print(first, second, sep='\n')
sum_ = deque()
first.reverse()
second.reverse()
i = 0
index = 0
if len(first) == len(second):
    i, index, sum_ = count_pattern(i, first, second, index, sum_)
    print(i, index, sum_, sep='\n')
    if index == 1:
        sum_.appendleft(hex(index)[2:].upper())
elif len(first) < len(second):
    i, index, sum_ = count_pattern(i, first, second, index, sum_)
    while i < len(second):
        sum_.appendleft(hex(int(second[i], 16) + index)[2:].upper())
        index = 0
        i += 1
else:
    first, second = second, first
    i, index, sum_ = count_pattern(i, first, second, index, sum_)
    while i < len(second):
        sum_.appendleft(hex(int(second[i], 16) + index)[2:].upper())
        index = 0
        i += 1
print(sum_)
