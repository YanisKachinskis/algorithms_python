# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input('Введите первую букву: ')
b = input('Введите вторую букву: ')
first_number = ord(a) - 96
second_number = ord(b) - 96
dif_number = abs(second_number - first_number) - 1

print(f'Номер первой буквы: {first_number}')
print(f'Номер второй буквы: {second_number}')
print(f'Число букв между ними: {dif_number}')
