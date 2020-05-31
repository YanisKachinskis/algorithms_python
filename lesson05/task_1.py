# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
# отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import defaultdict

QUARTERS = 4
total_income = 0
company_number = int(input("Введите количество предприятий: "))
total = defaultdict(list)
for company in range(1, company_number + 1):
    name = input(f'Введите название {company} предприятия: ')
    for quarter in range(1, QUARTERS + 1):
        income = int(input(f'Введите прибыль за {quarter} квартал: '))
        total[name].append(income)
        total_income += income
average_income = total_income / company_number
print(f"Средняя прибыль за год: {average_income}")

print(f'Предприятия с прибылью выше среднего:')
for i in total:
    if sum(total[i]) > average_income:
        print(f'{i}')

print(f'Предприятия с прибылью ниже среднего:')
for i in total:
    if sum(total[i]) < average_income:
        print(f'{i}')
