# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if c > a > b or b > a > c:
    print(a)
elif c > b > a or a > b > c:
    print(b)
else:
    print(c)
