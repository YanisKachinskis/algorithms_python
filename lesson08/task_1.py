# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.


import hashlib


def count_subs(text):
    n = 1
    text = text.replace(' ', '')
    s = []
    l = len(text)
    while n < l:
        i = 0
        while i < l and (i + n) <= l:
            temp = hashlib.sha1(text[i:i + n].encode('utf-8')).hexdigest()
            if temp not in s:
                s.append(temp)
            i += 1
        n += 1
    return len(s)


text = 'baobab'
print(f'Количество подстрок {count_subs(text)} в строке {text}.')

