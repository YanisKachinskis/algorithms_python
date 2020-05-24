# 2.Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать
# на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и
# попробуйте его улучшить/оптимизировать под задачу.
# # Второй — без использования «Решета Эратосфена».

import timeit
import cProfile
import math


# 1. Вариант с решетом Эратосфена:

def sieve_func(n):
    sieve = [i for i in range(int(n * math.log2(n)))]
    sieve[1] = 0
    # print(sieve)
    for i in range(2, int(n * math.log2(n))):
        if sieve[i] != 0:
            j = i + i
            while j < int(n * math.log2(n)):
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return f'Простое число {res[n - 1]} с порядковым номером {n}.'


print(timeit.timeit('sieve_func(50)', number=100, globals=globals()))  # 0.023100199999999998
print(timeit.timeit('sieve_func(100)', number=100, globals=globals()))  # 0.060253
print(timeit.timeit('sieve_func(150)', number=100, globals=globals()))  # 0.10372129999999999
print(timeit.timeit('sieve_func(200)', number=100, globals=globals()))  # 0.1473403


cProfile.run('sieve_func(50)')
#         1    0.000    0.000    0.000    0.000 task_2.py:15(sieve_func)
#         1    0.000    0.000    0.000    0.000 task_2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       539    0.000    0.000    0.000    0.000 {built-in method math.log2}
cProfile.run('sieve_func(100)')
#         1    0.001    0.001    0.001    0.001 task_2.py:15(sieve_func)
#         1    0.000    0.000    0.000    0.000 task_2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1369    0.000    0.000    0.000    0.000 {built-in method math.log2}
cProfile.run('sieve_func(150)')
#         1    0.001    0.001    0.002    0.002 task_2.py:15(sieve_func)
#         1    0.000    0.000    0.000    0.000 task_2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      2318    0.000    0.000    0.000    0.000 {built-in method math.log2}
cProfile.run('sieve_func(200)')
#         1    0.002    0.002    0.002    0.002 task_2.py:15(sieve_func)
#         1    0.000    0.000    0.000    0.000 task_2.py:16(<listcomp>)
#         1    0.000    0.000    0.000    0.000 task_2.py:25(<listcomp>)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      3345    0.001    0.000    0.001    0.000 {built-in method math.log2}


# 2. Вариант без решета Эратосфена:
START = 2


def prime_func(n):
    i = 1  # индекс простого числа
    k = 2  # счетчик чисел в целом начиная с 2
    while i <= n:
        j = 0
        while k % (START + j) != 0:
            j += 1
        if k == (START + j):
            prime_num = k
            i += 1
        k += 1
    return f'Простое число под номером {n} - это {prime_num}'

print(timeit.timeit('prime_func(50)', number=100, globals=globals()))  # 0.0549408
print(timeit.timeit('prime_func(100)', number=100, globals=globals()))  # 0.2749292
print(timeit.timeit('prime_func(150)', number=100, globals=globals()))  # 0.6886163000000001
print(timeit.timeit('prime_func(200)', number=100, globals=globals()))  # 1.3050723

cProfile.run('prime_func(50)')  # 1    0.001    0.001    0.001    0.001 task_2.py:47(prime_func)
cProfile.run('prime_func(100)')  # 1    0.003    0.003    0.003    0.003 task_2.py:47(prime_func)
cProfile.run('prime_func(150)')  # 1    0.007    0.007    0.007    0.007 task_2.py:47(prime_func)
cProfile.run('prime_func(200)')  # 1    0.013    0.013    0.013    0.013 task_2.py:47(prime_func)

# Вывод: Решето Эратосфена работает значительно быстрее второй функции.
# Временная оценка первого решения похожа на O(n), но учитывая, что диапазон изначального списка
# ближе всего к n*log2(n), то вероятно, если взять больше точек для анализа, то получим O(n * log2n).
# У второго алгоритма больше похоже на O(n^2).
