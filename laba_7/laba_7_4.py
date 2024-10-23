"""
Бондарева Варвара
Группа ИУ7-14Б
Лабораторная работа №7
Программа для замены двух подряд идущих
цифр на последнюю цифру их суммы
Вариант 6
"""

# Ввод значений и переменных
num_of_items = input('Введите количество элементов списка: ')
arr = list()

# Защита от хомяков - проверка количества элементов списка
while not num_of_items.isdigit() or num_of_items == '0':
    num_of_items = input('Количество элементов списка должно '
                         'быть целым положительным числом, попробуйте еще раз: ')
num_of_items = int(num_of_items)

# Создание списка строк
arr = [input('>> ') for i in range(num_of_items)]

# Основной цикл
for i in range(num_of_items):
    new = ''
    for char in range(len(arr[i]) - 1):
        if arr[i][char].isdigit() and arr[i][char + 1].isdigit():
            new += f'{(int(arr[i][char]) + int(arr[i][char + 1])) % 10}'
        else:
            new += arr[i][char]
    print(new)


# Вывод полученного списка
print(f'Полученный список: {arr}')
