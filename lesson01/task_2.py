# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

FIRST_LETTER = 96
letter_num = int(input('Введите номер буквы: '))
letter = chr(letter_num + FIRST_LETTER)
print(letter)
