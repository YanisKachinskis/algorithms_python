# https://drive.google.com/file/d/1hbNAbGUOD3F7vTWa8m051CTyRPypQhOB/view?usp=sharing
# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.


def reverse(a):
    if a < 10:
        return a
    else:
        return f'{a % 10}{reverse(a // 10)}'


a = int(input('Введите число: '))
print(int(reverse(a)))