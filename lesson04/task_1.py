# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например,
# если введено число 3486, надо вывести 6843.

import timeit
import cProfile


# 1. Решение задачи №1 (рекурсия)
DIV = 10


def reverse(a):
    if a < DIV:
        return a
    else:
        return f'{a % DIV}{reverse(a // DIV)}'


print(timeit.timeit('reverse(3486)', number=1000, globals=globals()))  # 0.0012572
print(timeit.timeit('reverse(3486952)', number=1000, globals=globals()))  # 0.002464099999999997
print(timeit.timeit('reverse(3486952123)', number=1000, globals=globals()))  # 0.003667700000000003
print(timeit.timeit('reverse(3486952123456)', number=1000, globals=globals()))  # 0.004939300000000001
print(timeit.timeit('reverse(3486952123456789)', number=1000, globals=globals()))  # 0.0063297999999999965

cProfile.run('reverse(3486)')  # 4/1    0.000    0.000    0.000    0.000 task_1.py:11(reverse)
cProfile.run('reverse(3486952)')  # 7/1    0.000    0.000    0.000    0.000 task_1.py:11(reverse)
cProfile.run('reverse(3486952123)')  # 10/1    0.000    0.000    0.000    0.000 task_1.py:11(reverse)
cProfile.run('reverse(3486952123456)')  # 13/1    0.000    0.000    0.000    0.000 task_1.py:11(reverse)
cProfile.run('reverse(3486952123456789)')  # 16/1    0.000    0.000    0.000    0.000 task_1.py:11(reverse)


# 2. Решение задачи №2 (цикл)


def reverse_loop(n):
    result = ''
    for i in range(len(str(n))):
        result = result + str(n % DIV)
        n = n // DIV
    return result


print(timeit.timeit('reverse_loop(3486)', number=1000, globals=globals()))  # 0.001995500000000004
print(timeit.timeit('reverse_loop(3486952)', number=1000, globals=globals()))  # 0.0030253000000000016
print(timeit.timeit('reverse_loop(3486952123)', number=1000, globals=globals()))  # 0.0042028
print(timeit.timeit('reverse_loop(3486952123456)', number=1000, globals=globals()))  # 0.005418299999999994
print(timeit.timeit('reverse_loop(3486952123456789)', number=1000, globals=globals()))  # 0.0067411

cProfile.run('reverse_loop(3486)')  # 1    0.000    0.000    0.000    0.000 task_1.py:36(reverse_loop)
cProfile.run('reverse_loop(3486952)')  # 1    0.000    0.000    0.000    0.000 task_1.py:36(reverse_loop)
cProfile.run('reverse_loop(3486952123)')  # 1    0.000    0.000    0.000    0.000 task_1.py:36(reverse_loop)
cProfile.run('reverse_loop(3486952123456)')  # 1    0.000    0.000    0.000    0.000 task_1.py:36(reverse_loop)
cProfile.run('reverse_loop(3486952123456789)')  # 1    0.000    0.000    0.000    0.000 task_1.py:36(reverse_loop)


# 3. Решение с циклом (усложненное)

def reverse_loop_hard(n):
    m = str(n)
    a = []
    len_num = 1
    while n > DIV:
        n //= DIV
        len_num += 1
    for i in range(len_num):
        h = int(m[i])
        if h == int(m[len_num - 1]):
            a.append(m[i])
        elif h < int(m[len_num - 1]):
            while h != int(m[len_num - 1]):
                h += 1
            a.append(str(h))
        else:
            while h != int(m[len_num - 1]):
                h -= 1
            a.append(str(h))
        len_num -= 1
        result = ''.join(a)
    return result


print(timeit.timeit('reverse_loop_hard(3486)', number=1000, globals=globals()))  # 0.009709599999999999
print(timeit.timeit('reverse_loop_hard(3486952)', number=1000, globals=globals()))  # 0.011051699999999998
print(timeit.timeit('reverse_loop_hard(3486952123)', number=1000, globals=globals()))  # 0.021937700000000004
print(timeit.timeit('reverse_loop_hard(3486952123456)', number=1000, globals=globals()))  # 0.02929839999999999
print(timeit.timeit('reverse_loop_hard(3486952123456789)', number=1000, globals=globals()))  # 0.031170999999999977

cProfile.run('reverse_loop_hard(3486)')
#         1    0.000    0.000    0.000    0.000 task_1.py:58(reverse_loop_hard)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         4    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         4    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('reverse_loop_hard(3486952)')
#         1    0.000    0.000    0.000    0.000 task_1.py:58(reverse_loop_hard)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         7    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         7    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('reverse_loop_hard(3486952123)')
#         1    0.000    0.000    0.000    0.000 task_1.py:58(reverse_loop_hard)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        10    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('reverse_loop_hard(3486952123456)')
#         1    0.000    0.000    0.000    0.000 task_1.py:58(reverse_loop_hard)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        13    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        13    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
cProfile.run('reverse_loop_hard(3486952123456789)')
#         1    0.000    0.000    0.000    0.000 task_1.py:58(reverse_loop_hard)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        16    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#        16    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}


# Вывод:
# 1. Вариант решается с помощью рекурсии. Проведено 5 тестов, на каждом число увеличивалось на 3 элемента.
# Время выполнения при этом увеличивалось приблизительно на одну и ту же величину. Количество вызываемых фуинкций
# увеличивается пропорционально длинне числа. Асимптотика алгоритма линейная O(n).

# 2. Вариант решения через цикл. Проведено 5 тестов, на каждом число увеличивалось свою длину на 3 элемента.
# Время выполнения при этом увеличивалось приблизительно на одну и ту же величину. В среднем время работы аналогично
# предыдущему варианту. Асимптотика алгоритма линейная O(n).

# 3. Вариант решения с несколькими циклами, как последовательными (для подсчета длинны числа), так и вложенными для
# для увеличения (или уменьшения) каждого последующего элемента (числа) до ему соответствующему с обратной стороны
# исходного числа + запись каждого нового числа в спсок и в итоге преобразование списка к строке через join,
# Ничего умней придумать не смог, чтоб ухудьшить алгоритм( Похоже просто выбрал неудачную задачу.
# Как итог получил нелинейную зависимость при увеличении порядка исходного числа. Время работы между разными замерами
# как увеличивается, так и уменьшается. Зависимость тут уже идет не только от длиины исходного числа, но и от конкретных
# цифр. С увеличением длинны числа так же увеличивается количество вызов методов join и append.
