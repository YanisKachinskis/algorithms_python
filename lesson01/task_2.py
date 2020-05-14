# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_num = int(input('Введите номер буквы: '))
letter = chr(letter_num + 96)
print(letter)
