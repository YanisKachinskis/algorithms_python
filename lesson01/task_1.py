# https://drive.google.com/file/d/1Q21BGKM6NVDU5Myx8SNkXtrbWQJVAXIx/view?usp=sharing
# ссылка на файл draw.io

# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

x = int(input('Введите трехзначное число: \n'))
a = x // 100  # первая цифра
b = (x // 10) % 10  # вторая цифра
c = x % 10  # третья цифра
print(f'Сумма цифр числа: {a + b + c}\nПроизведение цифр числа: {a * b * c}')
